# CardioDetect CSS Design Code Reference

## Complete CSS Implementation

This document contains the complete CSS styling code used in the CardioDetect UI/UX redesign.

---

## Location in Code

The CSS is placed at the beginning of `streamlit_app.py` (after imports and before page configuration):

```python
st.markdown("""
<style>
    [CSS CODE HERE]
</style>
""", unsafe_allow_html=True)
```

---

## CSS Color Variables

```css
:root {
    --bg-primary: #0f172a;          /* Deep Navy - Main background */
    --bg-secondary: #1a1f3a;        /* Charcoal - Cards & containers */
    --bg-tertiary: #232d4a;         /* Deep Slate - Hover states */
    --text-primary: #f1f5f9;        /* Off-white - Main text */
    --text-secondary: #cbd5e1;      /* Light Gray - Secondary text */
    --text-muted: #94a3b8;          /* Medium Gray - Muted text */
    --accent-primary: #ef4444;      /* Medical Red - Primary accent */
    --accent-secondary: #3b82f6;    /* Clinical Blue - Secondary accent */
    --success: #10b981;             /* Green - Success state */
    --warning: #f59e0b;             /* Amber - Warning state */
    --border-color: #334155;        /* Slate Gray - Borders */
}
```

---

## Base Styles

```css
* {
    box-sizing: border-box;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg-primary);
    color: var(--text-primary);
}

.main {
    background-color: var(--bg-primary);
    padding-top: 1.5rem;
}
```

---

## Header Styling

```css
.header-container {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    padding: 2.5rem 2rem;
    border-radius: 12px;
    color: var(--text-primary);
    margin-bottom: 2.5rem;
    border: 1px solid var(--border-color);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.header-container h1 {
    margin: 0;
    font-size: 2.2rem;
    font-weight: 600;
    letter-spacing: -0.3px;
    color: var(--text-primary);
}

.header-container p {
    margin: 0.75rem 0 0 0;
    font-size: 1rem;
    color: var(--text-secondary);
    font-weight: 400;
}
```

---

## Tab Navigation

```css
.stTabs {
    margin-top: 0;
}

.stTabs [data-baseweb="tab-list"] {
    border-bottom: 1px solid var(--border-color);
}

.stTabs [data-baseweb="tab-list"] button {
    font-size: 0.95rem;
    font-weight: 500;
    padding: 1rem 1.25rem;
    border-radius: 8px 8px 0 0;
    transition: all 0.2s ease;
    color: var(--text-muted);
    border: none;
    background: transparent;
}

.stTabs [data-baseweb="tab-list"] button:hover {
    color: var(--text-secondary);
    background-color: rgba(148, 163, 184, 0.1);
}

.stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
    color: var(--accent-primary);
    border-bottom: 2px solid var(--accent-primary);
    background: transparent;
}
```

---

## Card Components

```css
.card {
    background: linear-gradient(135deg, #1a1f3a 0%, #232d4a 100%);
    padding: 1.75rem;
    border-radius: 10px;
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    transition: all 0.2s ease;
}

.card:hover {
    border-color: rgba(239, 68, 68, 0.3);
    box-shadow: 0 8px 24px rgba(239, 68, 68, 0.1);
}

.metric-card {
    background: linear-gradient(135deg, #1a1f3a 0%, #232d4a 100%);
    padding: 1.5rem;
    border-radius: 10px;
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    text-align: center;
}

.metric-card h3 {
    margin: 0 0 0.5rem 0;
    font-size: 1.75rem;
    font-weight: 600;
    color: var(--accent-primary);
}

.metric-card p {
    margin: 0;
    font-size: 0.85rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.input-section {
    background: linear-gradient(135deg, #1a1f3a 0%, #232d4a 100%);
    padding: 2rem;
    border-radius: 10px;
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    margin-bottom: 2rem;
}
```

---

## Section Titles

```css
.section-title {
    color: var(--text-primary);
    font-size: 1.4rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid var(--border-color);
}
```

---

## Risk Level Styling

```css
.risk-low {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(16, 185, 129, 0.05) 100%);
    border-left: 4px solid #10b981;
    padding: 1.5rem;
    border-radius: 10px;
    color: #86efac;
}

.risk-low h3 {
    margin-top: 0;
    margin-bottom: 0.5rem;
    color: #10b981;
}

.risk-moderate {
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(245, 158, 11, 0.05) 100%);
    border-left: 4px solid #f59e0b;
    padding: 1.5rem;
    border-radius: 10px;
    color: #fbbf24;
}

.risk-moderate h3 {
    margin-top: 0;
    margin-bottom: 0.5rem;
    color: #f59e0b;
}

.risk-high {
    background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(239, 68, 68, 0.05) 100%);
    border-left: 4px solid #ef4444;
    padding: 1.5rem;
    border-radius: 10px;
    color: #fca5a5;
}

.risk-high h3 {
    margin-top: 0;
    margin-bottom: 0.5rem;
    color: #ef4444;
}
```

---

## Button Styling

```css
.stButton > button {
    border-radius: 8px;
    padding: 0.75rem 1.75rem;
    font-weight: 500;
    border: none;
    transition: all 0.2s ease;
    font-size: 0.95rem;
    letter-spacing: 0.3px;
}

.stButton > button:first-child {
    background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
    color: white;
    box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
}

.stButton > button:first-child:hover {
    box-shadow: 0 8px 24px rgba(239, 68, 68, 0.4);
    transform: translateY(-2px);
}

.stButton > button:nth-child(2) {
    background: linear-gradient(135deg, #334155 0%, #1e293b 100%);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
}

.stButton > button:nth-child(2):hover {
    background: linear-gradient(135deg, #475569 0%, #334155 100%);
}
```

---

## Input Elements

```css
.stSlider [data-testid="stTickBar"] {
    background: var(--border-color);
}
```

---

## Sidebar

```css
.stSidebar {
    background: linear-gradient(180deg, #1a1f3a 0%, #232d4a 100%);
    border-right: 1px solid var(--border-color);
}

.stSidebar .stMarkdown {
    color: var(--text-primary);
}

.stSidebar [data-testid="stMarkdownContainer"] {
    color: var(--text-secondary);
}
```

---

## Information Boxes

```css
.info-box {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(59, 130, 246, 0.05) 100%);
    border-left: 4px solid #3b82f6;
    padding: 1.25rem;
    border-radius: 8px;
    color: #93c5fd;
    font-size: 0.95rem;
}
```

---

## Metrics

```css
.stMetric {
    background: linear-gradient(135deg, #1a1f3a 0%, #232d4a 100%);
    padding: 1.5rem;
    border-radius: 10px;
    border: 1px solid var(--border-color);
}

[data-testid="metric-container"] {
    background: linear-gradient(135deg, #1a1f3a 0%, #232d4a 100%);
    padding: 1.5rem;
    border-radius: 10px;
    border: 1px solid var(--border-color);
}

[data-testid="metric-container"] [data-testid="stMetricLabel"] {
    color: var(--text-muted);
    font-size: 0.8rem;
}

[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: var(--accent-primary);
    font-size: 1.8rem;
}
```

---

## Expanders

```css
.streamlit-expanderHeader {
    background: linear-gradient(135deg, #1a1f3a 0%, #232d4a 100%);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    color: var(--text-primary);
}

.streamlit-expanderHeader:hover {
    border-color: rgba(239, 68, 68, 0.3);
}

.streamlit-expanderContent {
    background: linear-gradient(135deg, #232d4a 0%, #1a1f3a 100%);
    border: 1px solid var(--border-color);
    border-top: none;
    border-radius: 0 0 8px 8px;
    padding: 1rem;
}
```

---

## Data Frame

```css
.stDataFrame {
    border-radius: 8px;
    overflow: hidden;
}

[data-testid="stDataFrame"] {
    background: linear-gradient(135deg, #1a1f3a 0%, #232d4a 100%);
}
```

---

## Progress Bar

```css
.stProgress > div > div > div > div {
    background-color: var(--accent-primary);
    border-radius: 4px;
}

.stProgress > div > div > div {
    background-color: var(--bg-tertiary);
    border-radius: 4px;
    border: 1px solid var(--border-color);
}
```

---

## Alerts

```css
[data-testid="stAlert"] {
    background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(239, 68, 68, 0.05) 100%);
    border: 1px solid rgba(239, 68, 68, 0.3);
    border-radius: 8px;
    color: #fca5a5;
}
```

---

## Dividers & Separators

```css
hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border-color), transparent);
    margin: 2rem 0;
}
```

---

## Typography

```css
h1, h2, h3, h4, h5, h6 {
    color: var(--text-primary) !important;
}

p, label, span {
    color: var(--text-secondary) !important;
}

a {
    color: #3b82f6 !important;
}

a:hover {
    color: #60a5fa !important;
}
```

---

## Usage Guide

### Applying to Components

1. **Section Headers**:
   ```html
   <div class="section-title">Assessment Results</div>
   ```

2. **Cards**:
   ```html
   <div class="card">Content here</div>
   ```

3. **Risk Assessment**:
   ```html
   <div class="risk-low">No Heart Disease Detected</div>
   <!-- or -->
   <div class="risk-high">Heart Disease Risk Detected</div>
   ```

4. **Information Boxes**:
   ```html
   <div class="info-box">Important information here</div>
   ```

---

## Color Scheme

### Dark Theme Colors
| Usage | Color | Code |
|-------|-------|------|
| Main Background | Deep Navy | #0f172a |
| Cards & Containers | Charcoal | #1a1f3a |
| Hover States | Deep Slate | #232d4a |
| Primary Text | Off-white | #f1f5f9 |
| Secondary Text | Light Gray | #cbd5e1 |
| Muted Text | Medium Gray | #94a3b8 |
| Primary Accent | Medical Red | #ef4444 |
| Secondary Accent | Clinical Blue | #3b82f6 |
| Success | Green | #10b981 |
| Warning | Amber | #f59e0b |
| Borders | Slate Gray | #334155 |

---

## Responsive Design

The design is responsive and adapts to different screen sizes through Streamlit's built-in responsive grid system using `st.columns()`.

---

## Browser Compatibility

- ✅ Chrome/Chromium
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers

---

## Performance Considerations

- No external CSS files (inline styling)
- No JavaScript required
- CSS-only animations
- Minimal DOM overhead
- Fast rendering

---

## Customization Tips

### Change Accent Color
Replace `#ef4444` (red) with desired color throughout:
- Primary buttons
- Risk-high sections
- Tab indicators

### Adjust Dark Mode Intensity
Modify background colors:
- Lighter: Use `#1a2a4a` instead of `#0f172a`
- Darker: Use `#080d1a` for even darker feel

### Font Customization
Add custom fonts in page config:
```python
st.set_page_config(
    page_title="...",
    page_icon="...",
)
```

---

## Design References

This design follows:
- **Modern Dashboard Trends**: Clean, minimalist, dark theme
- **Medical Design Principles**: Professional, trustworthy appearance
- **Accessibility Standards**: WCAG 2.1 AA contrast ratios
- **User Experience Best Practices**: Clear hierarchy, intuitive layout

---

**Last Updated**: January 29, 2026
**Version**: 1.0.0
**Status**: ✅ Production Ready
