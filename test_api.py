"""
CardioPredict - API Test Suite
Test the prediction endpoint with sample patient data
"""

import requests
import json
import time

BASE_URL = "http://localhost:5000"

# Sample patient data - High risk
HIGH_RISK_PATIENT = {
    "age": "75",
    "sex": "1",
    "cp": "3",
    "trestbps": "160",
    "chol": "320",
    "fbs": "1",
    "restecg": "2",
    "thalach": "90",
    "exang": "1",
    "oldpeak": "5.0",
    "slope": "2",
    "ca": "3",
    "thal": "2",
    "chest_pain_type": "3",
    "blood_pressure": "110",
    "cholesterol": "340",
    "heart_rate": "85",
    "st_depression": "8.0"
}

# Sample patient data - Low risk
LOW_RISK_PATIENT = {
    "age": "35",
    "sex": "0",
    "cp": "0",
    "trestbps": "120",
    "chol": "180",
    "fbs": "0",
    "restecg": "0",
    "thalach": "160",
    "exang": "0",
    "oldpeak": "0.0",
    "slope": "1",
    "ca": "0",
    "thal": "0",
    "chest_pain_type": "0",
    "blood_pressure": "80",
    "cholesterol": "190",
    "heart_rate": "70",
    "st_depression": "0.0"
}

# Sample patient data - Moderate risk
MODERATE_RISK_PATIENT = {
    "age": "55",
    "sex": "1",
    "cp": "1",
    "trestbps": "130",
    "chol": "240",
    "fbs": "0",
    "restecg": "1",
    "thalach": "150",
    "exang": "0",
    "oldpeak": "1.5",
    "slope": "1",
    "ca": "1",
    "thal": "2",
    "chest_pain_type": "1",
    "blood_pressure": "85",
    "cholesterol": "250",
    "heart_rate": "75",
    "st_depression": "0.5"
}


def test_health_endpoint():
    """Test health check endpoint"""
    print("\n" + "="*60)
    print("Testing Health Endpoint")
    print("="*60)
    
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        data = response.json()
        
        print(f"✓ Status Code: {response.status_code}")
        print(f"✓ Server Status: {data['status']}")
        print(f"✓ Model Loaded: {data['model_loaded']}")
        print(f"✓ Scaler Loaded: {data['scaler_loaded']}")
        
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_prediction(patient_data, patient_name):
    """Test prediction endpoint with patient data"""
    print(f"\n{'='*60}")
    print(f"Testing Prediction - {patient_name}")
    print("="*60)
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/predict",
            json=patient_data,
            timeout=10
        )
        
        if response.status_code != 200:
            print(f"✗ Error: HTTP {response.status_code}")
            print(f"✗ Response: {response.text}")
            return False
        
        data = response.json()
        
        if not data.get('success'):
            print(f"✗ Prediction failed: {data.get('error')}")
            return False
        
        print(f"\n✓ Prediction successful!")
        print(f"\nResults:")
        print(f"  Diagnosis: {data['diagnosis']}")
        print(f"  Risk Percentage: {data['risk_percentage']}%")
        print(f"  Confidence: {data['confidence']}%")
        print(f"\nProbabilities:")
        print(f"  Healthy: {data['probabilities']['healthy']}%")
        print(f"  Diseased: {data['probabilities']['diseased']}%")
        print(f"\nSHAP Plot Generated: {bool(data['shap_plot'])}")
        
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_feature_info():
    """Test feature information endpoint"""
    print("\n" + "="*60)
    print("Testing Feature Info Endpoint")
    print("="*60)
    
    try:
        response = requests.get(f"{BASE_URL}/api/feature-info", timeout=5)
        data = response.json()
        
        print(f"✓ Status Code: {response.status_code}")
        print(f"✓ Features Available: {len(data)}")
        
        # Show first 3 features
        count = 0
        for feature_name, feature_info in data.items():
            if count >= 3:
                break
            print(f"\n  - {feature_name}:")
            print(f"    Label: {feature_info.get('label')}")
            print(f"    Type: {feature_info.get('type')}")
            print(f"    Unit: {feature_info.get('unit')}")
            count += 1
        
        print(f"\n  ... and {len(data) - 3} more features")
        
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def run_all_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("CardioPredict - API Test Suite")
    print("="*60)
    print("\nMake sure Flask server is running on http://localhost:5000")
    print("Run: python app.py")
    
    input("\nPress Enter to start tests...")
    
    results = []
    
    # Test health
    results.append(("Health Check", test_health_endpoint()))
    time.sleep(1)
    
    # Test feature info
    results.append(("Feature Info", test_feature_info()))
    time.sleep(1)
    
    # Test predictions
    results.append(("Low Risk Patient", test_prediction(LOW_RISK_PATIENT, "Low Risk Patient")))
    time.sleep(1)
    
    results.append(("Moderate Risk Patient", test_prediction(MODERATE_RISK_PATIENT, "Moderate Risk Patient")))
    time.sleep(1)
    
    results.append(("High Risk Patient", test_prediction(HIGH_RISK_PATIENT, "High Risk Patient")))
    
    # Summary
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n✓ All tests passed! System is working correctly.")
    else:
        print(f"\n✗ {total - passed} test(s) failed. Check server and try again.")


if __name__ == "__main__":
    run_all_tests()
