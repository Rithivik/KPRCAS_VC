# 🎨 KPRCAS Chatbot - Color Reference Card

## Color Palette

```
┌─────────────────────────────────────┐
│ PRIMARY BLUE                        │
│ #1e3a8c                            │
│ Used in: Bot text, Header          │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ PRIMARY GREEN                       │
│ #2d8659                            │
│ Used in: Send button, Input,       │
│         User messages, Buttons     │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ LIGHT GREEN                         │
│ #e8f5f0                            │
│ Used in: Bot message background    │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ WHITE                               │
│ #ffffff                            │
│ Used in: Backgrounds, Text         │
└─────────────────────────────────────┘
```

---

## Element Color Map

| Element | Color | Hex | Example |
|---------|-------|-----|---------|
| 📍 Header | Gradient | #1e3a8c → #2d8659 | Top banner |
| 💬 Your Message | Green | #2d8659 | Right-aligned bubble |
| 🤖 Bot Message | Light Green | #e8f5f0 | Left-aligned bubble with blue text |
| ⬆️ Send Button | Green | #2d8659 | Circle button with arrow |
| ✏️ Input Field | Green Border | #2d8659 | Text input box |
| 🏷️ Quick Replies | Green Border | #2d8659 | Clickable suggestion chips |
| ⏳ Typing Dots | Green | #2d8659 | Three animated circles |
| 📜 Scrollbar | Green | #2d8659 | Vertical scroll bar |
| 🎓 Watermark | Subtle | opacity: 0.08 | Logo in background |

---

## CSS Color Values Quick Reference

```css
/* Blue Shades */
--blue-primary: #1e3a8c;
--blue-dark: #152841;

/* Green Shades */
--green-primary: #2d8659;
--green-light: #e8f5f0;
--green-dark: #1f5f3f;

/* Neutrals */
--white: #ffffff;
--text-dark: #1e3a8c;
--text-muted: #5a9976;
```

---

## Quick Edit Guide

### To change green to different color:
```
Find: #2d8659
Replace: YOUR_COLOR_CODE
```

### To change blue to different color:
```
Find: #1e3a8c
Replace: YOUR_COLOR_CODE
```

### To make watermark more/less visible:
```css
.watermark { 
  opacity: 0.08;  /* Change this number */
  /* 0.05 = more subtle */
  /* 0.15 = more visible */
  /* 0.25 = very prominent */
}
```

---

## Live Preview

### Header
```
╔═══════════════════════════════════════╗
║ 🎓 KPRCAS VC 🟢                      ║  ← Blue-Green gradient
║ KPR College Virtual Assistant       ║
╚═══════════════════════════════════════╝
```

### Chat Window
```
┌────────────────────────────────────┐
│          [Watermark Logo]          │  ← Subtle background (8% opacity)
│                                    │
│ 🎓 Hi! How can I help?             │  ← Light green bubble (blue text)
│ Just now                           │
│                                    │
│                Can I help you? ✅  │  ← Green bubble (white text)
│                       5:30 PM      │
│                                    │
│ [Programs] [Admissions] [Campus]   │  ← Green bordered buttons
└────────────────────────────────────┘

┌────────────────────────────────────┐
│ 📝 Type a message...          [➜]  │  ← Green border + button
└────────────────────────────────────┘
```

---

## Color Testing

To verify colors are applied:

1. ✅ Header is **blue-to-green gradient**
2. ✅ Send button is **green** (#2d8659)
3. ✅ Input border is **green**
4. ✅ Your messages are **green** background
5. ✅ Bot messages are **light green** background
6. ✅ Buttons are **green bordered**
7. ✅ Scrollbar is **green**
8. ✅ Logo watermark **barely visible** in center

---

## Design System

**Primary Brand Colors**
- Blue: Used for headers and text emphasis
- Green: Used for interactive elements and user actions

**Hierarchy**
1. **Interactive** (Green) - Buttons, inputs, user messages
2. **Content** (Light Green) - Bot messages
3. **Text** (Blue) - Bot response text
4. **Background** (White) - Chat area

**Contrast Ratios**
- Green on white: ✅ Accessible
- Blue on white: ✅ Accessible
- White on green: ✅ Accessible
- White on blue: ✅ Accessible

---

## Theme Files

**Modified:** `static/style.css`
- All color values updated
- Watermark CSS added
- Gradient definitions

**Modified:** `templates/index.html`
- Watermark div added
- Logo images updated

**Modified:** `static/script.js`
- Avatar image references updated

---

## Watermark Details

```css
.watermark {
  position: absolute;        /* Stays in place */
  top: 50%;                  /* Centered vertically */
  left: 50%;                 /* Centered horizontally */
  transform: translate(-50%, -50%);  /* Adjustment */
  width: 180px;              /* Logo size */
  height: 180px;
  opacity: 0.08;             /* 8% visible (91% transparent) */
  pointer-events: none;      /* Doesn't block clicks */
  z-index: 0;                /* Behind messages */
}
```

---

**Your chatbot now features official KPRCAS branding!** 🎓💙💚

Download **KPRCAS_VC_Final.zip** and enjoy! ✨
