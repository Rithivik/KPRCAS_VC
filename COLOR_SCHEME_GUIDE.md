# 🎨 KPRCAS Chatbot - Color Scheme & Watermark Update

## Complete Color Transformation ✨

Your chatbot now features the official **KPRCAS color scheme**:

- **Primary Blue**: `#1e3a8c` (Dark blue from logo)
- **Primary Green**: `#2d8659` (Green from logo)
- **White**: `#ffffff` (Background)
- **Light Green**: `#e8f5f0` (Bot message background)
- **Dark Text**: `#1e3a8c` (Text on light backgrounds)

---

## Color Application Guide

### 🔵 Blue (#1e3a8c)
- Bot message text color
- Used for text that needs emphasis
- Dark blue accent for depth

### 💚 Green (#2d8659)
- **Send button** - Click to send message
- **Chat input border** - Input field outline
- **User message bubbles** - Your messages
- **Quick reply chips** - Suggestion buttons on hover
- **Scrollbar** - Chat window scroll indicator
- **Typing indicator** - Three animated dots

### ⚪ White & Light Green
- **Chat background** - Clean white with subtle green tint
- **Bot message bubbles** - Light green background (#e8f5f0)
- **Header background** - Blue-to-green gradient

---

## 🎭 Watermark Logo

The KPRCAS logo now appears as a **semi-transparent watermark** in the center of the chat window!

### Watermark Details
- **Position**: Center of chat window
- **Opacity**: 8% (very subtle, doesn't interfere with reading)
- **Size**: 180px × 180px
- **Visibility**: Always visible but not distracting
- **Layer**: Behind all messages

### CSS Implementation
```css
.watermark {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 180px;
  height: 180px;
  opacity: 0.08;
  pointer-events: none;
  z-index: 0;
}
```

---

## Color-Coded Elements

| Element | Color | Hex | Purpose |
|---------|-------|-----|---------|
| Header Gradient | Blue → Green | #1e3a8c → #2d8659 | Top banner |
| User Messages | Green | #2d8659 | Your message bubbles |
| Bot Messages | Light Green | #e8f5f0 | AI response bubbles |
| Send Button | Green | #2d8659 | Send message action |
| Input Field | Green Border | #2d8659 | Type here |
| Quick Replies | Green Border | #2d8659 | Suggestion buttons |
| Scrollbar | Green | #2d8659 | Scroll indicator |
| Typing Dots | Green | #2d8659 | "Bot is typing..." |
| Watermark Logo | Subtle | opacity: 0.08 | Background watermark |

---

## Visual Hierarchy

### Primary Actions (Green)
- ✅ Send button
- ✅ Input field
- ✅ Quick reply buttons
- ✅ Hover states

### Information (Blue)
- ℹ️ Bot responses
- ℹ️ Header text
- ℹ️ Logo branding

### Background (White/Light)
- 📄 Chat background
- 📄 Message bubbles
- 📄 Input area

---

## Updated HTML Elements

### 1. Chat Header
```html
<div class="chat-header">
  <!-- Logo image -->
  <img src="/static/kprcas_logo.png" class="avatar" alt="KPRCAS Logo">
  <!-- Text info -->
  <div class="header-info">
    <h1>KPRCAS VC <span class="online-dot"></span></h1>
    <p>KPR College Virtual Assistant · Online</p>
  </div>
</div>
```
**Colors**: Blue-to-green gradient, white text

### 2. Chat Window with Watermark
```html
<div class="chat-window">
  <!-- Watermark logo -->
  <div class="watermark">
    <img src="/static/kprcas_logo.png" alt="KPRCAS Watermark">
  </div>
  <!-- Messages appear here -->
</div>
```
**Colors**: White background, subtle watermark, light green bubbles

### 3. Input Area
```html
<div class="chat-input-area">
  <input type="text" id="userInput" placeholder="Type a message...">
  <button id="sendBtn">→</button>
</div>
```
**Colors**: Green border (#2d8659), green button

---

## CSS Color Updates

### Header
```css
.chat-header {
  background: linear-gradient(135deg, #1e3a8c, #2d8659);
  color: #fff;
}
```

### Send Button
```css
#sendBtn {
  background: #2d8659;  /* Green */
}

#sendBtn:hover {
  background: #1f5f3f;  /* Darker green */
}
```

### User Messages
```css
.message.user .bubble {
  background: #2d8659;  /* Green */
  color: #fff;
}
```

### Bot Messages
```css
.message.bot .bubble {
  background: #e8f5f0;  /* Light green */
  color: #1e3a8c;       /* Blue text */
}
```

### Input Field
```css
#userInput {
  border: 1px solid #2d8659;  /* Green border */
}

#userInput:focus {
  border-color: #2d8659;  /* Green on focus */
  box-shadow: 0 0 0 3px rgba(45, 134, 89, 0.1);  /* Subtle glow */
}
```

### Quick Reply Buttons
```css
.chip {
  border: 2px solid #2d8659;
  color: #2d8659;
}

.chip:hover {
  background: #2d8659;
  color: #fff;
}
```

### Scrollbar
```css
.chat-window::-webkit-scrollbar-thumb {
  background: #2d8659;  /* Green */
}
```

### Watermark Logo
```css
.watermark {
  opacity: 0.08;  /* Very subtle */
  pointer-events: none;  /* Doesn't interfere with interaction */
}
```

---

## Before & After

### BEFORE
- Plain blue color scheme
- Generic appearance
- No watermark
- No visual connection to college branding

### AFTER ✨
- **KPRCAS branded colors** (blue & green)
- **Professional appearance** aligned with college logo
- **Elegant watermark** - KPRCAS logo subtly in background
- **Cohesive design** - Every element matches color scheme
- **Better UX** - Green highlights draw attention to actions

---

## Customization Options

### Adjust Watermark Opacity
In `style.css`, change `.watermark { opacity: 0.08; }` to:
- `0.05` - More subtle
- `0.15` - More visible
- `0.25` - Very prominent

### Adjust Watermark Size
Change `.watermark { width: 180px; height: 180px; }` to:
- `150px 150px` - Smaller
- `250px 250px` - Larger

### Change Green to Different Color
Replace `#2d8659` with any hex color:
```css
/* Replace all instances of #2d8659 with your color */
#sendBtn { background: #your-color; }
.chip { border: 2px solid #your-color; }
/* etc. */
```

---

## File Changes Summary

### Modified Files
1. **style.css** - All color updates, watermark CSS
2. **index.html** - Added watermark div, logo images
3. **script.js** - Updated avatar images

### Color Values Used
```
Primary Blue:  #1e3a8c
Primary Green: #2d8659
Light Green:   #e8f5f0
White:         #ffffff
Dark Text:     #1e3a8c
```

---

## Testing Checklist

After running the chatbot, verify:

✅ Header shows blue-to-green gradient  
✅ Send button is green  
✅ Input field has green border  
✅ Your messages appear in green  
✅ Bot messages have light green background  
✅ Quick reply buttons have green borders  
✅ Watermark logo visible in center (barely visible)  
✅ Scrollbar is green  
✅ Typing indicator dots are green  

---

## Browser Compatibility

These colors and watermark work in:
- ✅ Chrome (Latest)
- ✅ Firefox (Latest)
- ✅ Safari (Latest)
- ✅ Edge (Latest)

---

## Next Steps

1. ✅ Extract `KPRCAS_VC_Final.zip`
2. ✅ Add `.env` with your API key
3. ✅ Run `python app.py`
4. ✅ Open `http://localhost:5000`
5. ✅ Admire the beautiful KPRCAS-branded chatbot! 🎓

---

## Contact & Support

If you want to further customize colors:
1. Edit `static/style.css` directly
2. Search for hex codes: `#2d8659` (green), `#1e3a8c` (blue)
3. Replace with your preferred colors
4. Refresh browser to see changes

**Enjoy your branded chatbot!** 💙💚✨
