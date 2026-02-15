# EasyAgri AI - Design Guidelines

## Design Philosophy

EasyAgri AI is designed with **rural farmers** as the primary users. Our design principles prioritize accessibility, simplicity, and effectiveness for users with varying levels of digital literacy.

## Core Design Principles

### 1. **Simplicity First**
- Minimize cognitive load
- Use familiar patterns and metaphors
- Avoid complex navigation structures
- Clear visual hierarchy

### 2. **Accessibility**
- Large, touchable UI elements (minimum 44x44 points)
- High contrast text for outdoor visibility
- Voice-first interface for low-literacy users
- Support for multiple Indian languages

### 3. **Offline-First**
- Core features work without internet
- Clear indicators for online/offline status
- Graceful degradation of features
- Local data caching

### 4. **Performance**
- Fast loading times (<2 seconds)
- Optimized images and assets
- Lazy loading for non-critical content
- Minimal battery consumption

### 5. **Cultural Sensitivity**
- Use locally relevant imagery
- Respect regional crop preferences
- Culturally appropriate colors
- Local language support (not just translation)

## Visual Design System

### Color Palette

**Primary Colors:**
```
Green (Agriculture):   #2E7D32  // Primary actions, success
Light Green:           #4CAF50  // Highlights
Accent Green:          #81C784  // Secondary elements
```

**Secondary Colors:**
```
Blue (Water/Sky):      #1976D2  // Information, weather
Orange (Sun/Growth):   #FF9800  // Warnings, alerts
Brown (Soil/Earth):    #6D4C41  // Grounded elements
```

**Neutral Colors:**
```
Dark Gray (Text):      #212121
Medium Gray:           #757575
Light Gray:            #BDBDBD
Background:            #FAFAFA
White:                 #FFFFFF
```

**Semantic Colors:**
```
Success:               #4CAF50
Warning:               #FF9800
Error:                 #F44336
Info:                  #2196F3
```

### Typography

**Font Family:**
- **Primary:** Noto Sans (supports multiple Indian languages)
- **Secondary:** Roboto
- **Monospace:** Roboto Mono (for codes, numbers)

**Font Sizes:**
```
Heading 1:    32px / 2rem  (bold)
Heading 2:    24px / 1.5rem (bold)
Heading 3:    20px / 1.25rem (semibold)
Body Large:   18px / 1.125rem (regular)
Body:         16px / 1rem (regular)
Small:        14px / 0.875rem (regular)
Caption:      12px / 0.75rem (regular)
```

**Line Heights:**
```
Headings:     1.2
Body:         1.5
```

### Spacing System

Based on 8px grid:
```
xs:  4px   (0.25rem)
sm:  8px   (0.5rem)
md:  16px  (1rem)
lg:  24px  (1.5rem)
xl:  32px  (2rem)
2xl: 48px  (3rem)
3xl: 64px  (4rem)
```

### Icons

**Icon Set:** Material Icons / Lucide React

**Icon Sizes:**
```
Small:   16px
Medium:  24px
Large:   32px
XLarge:  48px
```

**Guidelines:**
- Use filled icons for active states
- Use outlined icons for inactive states
- Maintain consistent stroke width
- Pair icons with text labels for clarity

## Component Design

### Buttons

**Primary Button:**
```jsx
Background: #2E7D32
Text: #FFFFFF
Height: 48px
Border Radius: 8px
Font Weight: 600
Min Width: 120px
```

**Secondary Button:**
```jsx
Background: transparent
Border: 2px solid #2E7D32
Text: #2E7D32
Height: 48px
Border Radius: 8px
```

**States:**
- Default
- Hover (darken 10%)
- Active (darken 20%)
- Disabled (opacity 50%)

### Input Fields

```jsx
Height: 48px
Border: 1px solid #BDBDBD
Border Radius: 8px
Padding: 12px 16px
Font Size: 16px
```

**States:**
- Default
- Focus (border: #2E7D32, 2px)
- Error (border: #F44336, 2px)
- Disabled (background: #F5F5F5)

### Cards

```jsx
Background: #FFFFFF
Border Radius: 12px
Padding: 16px
Shadow: 0 2px 8px rgba(0,0,0,0.1)
```

### Navigation

**Bottom Tab Bar (Mobile):**
```jsx
Height: 64px
Background: #FFFFFF
Shadow: 0 -2px 8px rgba(0,0,0,0.1)
Icon Size: 24px
Label Font: 12px
```

**Active Tab:**
- Icon color: #2E7D32
- Label color: #2E7D32
- Font weight: 600

**Inactive Tab:**
- Icon color: #757575
- Label color: #757575
- Font weight: 400

## Screen Layouts

### Home Dashboard

```
┌─────────────────────────┐
│  Header (EasyAgri AI)   │
├─────────────────────────┤
│  Weather Widget         │
├─────────────────────────┤
│  ┌─────┐  ┌─────┐       │
│  │Crop │  │Irri-│       │
│  │Health│  │gation│      │
│  └─────┘  └─────┘       │
│  ┌─────┐  ┌─────┐       │
│  │Market│  │Weather│     │
│  │Price │  │       │     │
│  └─────┘  └─────┘       │
│  ┌─────┐  ┌─────┐       │
│  │Comm. │  │Schemes│     │
│  └─────┘  └─────┘       │
├─────────────────────────┤
│  Bottom Navigation      │
└─────────────────────────┘
```

### Disease Detection Screen

```
┌─────────────────────────┐
│  ← Crop Health          │
├─────────────────────────┤
│                         │
│    Camera Preview       │
│    Area (280px)         │
│                         │
├─────────────────────────┤
│     [Capture 📸]        │
├─────────────────────────┤
│  Instructions:          │
│  1. Focus on leaf       │
│  2. Good lighting       │
│  3. Take clear photo    │
│                         │
├─────────────────────────┤
│  🎤 Voice Help          │
└─────────────────────────┘
```

## Responsive Design

### Breakpoints

```
Mobile:      320px - 767px
Tablet:      768px - 1023px
Desktop:     1024px+
```

### Mobile-First Approach

Design for mobile first, then scale up:
1. Start with mobile layout
2. Add tablet adaptations
3. Optimize for desktop

## Accessibility Guidelines

### WCAG 2.1 Level AA Compliance

**Color Contrast:**
- Normal text: 4.5:1 minimum
- Large text (18px+): 3:1 minimum
- UI components: 3:1 minimum

**Touch Targets:**
- Minimum size: 44x44 pixels
- Spacing between: 8px minimum

**Screen Reader Support:**
- Meaningful alt text for images
- ARIA labels for interactive elements
- Proper heading hierarchy
- Focus indicators

**Keyboard Navigation:**
- Logical tab order
- Skip to content links
- Visible focus states

### Voice Interface Design

**Voice Commands:**
```
"Open crop health"
"Check market prices for rice"
"Show weather forecast"
"Apply for PM-KISAN"
```

**Voice Feedback:**
- Confirm actions audibly
- Provide clear error messages
- Guide users through multi-step processes

## Iconography

### Icon Style

- Outline style for consistency
- 2px stroke width
- Rounded corners (2px radius)
- Balanced proportions

### Icon Usage

**Crop Health:** 🔬 Microscope
**Irrigation:** 💧 Water Drop
**Market:** 📊 Chart
**Weather:** 🌤️ Sun/Cloud
**Community:** 👥 People
**Schemes:** 🏛️ Building
**Settings:** ⚙️ Gear
**Profile:** 👤 Person

## Animation & Motion

### Principles

1. **Purposeful:** Every animation has a reason
2. **Fast:** 200-300ms for most transitions
3. **Natural:** Use easing functions
4. **Subtle:** Don't distract from content

### Timing Functions

```
Ease Out:    cubic-bezier(0.0, 0.0, 0.2, 1)
Ease In:     cubic-bezier(0.4, 0.0, 1, 1)
Ease In Out: cubic-bezier(0.4, 0.0, 0.2, 1)
```

### Common Animations

**Screen Transitions:**
```
Duration: 250ms
Easing: ease-in-out
```

**Button Press:**
```
Duration: 100ms
Scale: 0.95
```

**Loading Spinner:**
```
Duration: 1000ms
Rotation: 360deg
```

## Image Guidelines

### Photo Requirements

**Crop Images:**
- Format: JPEG
- Max size: 5MB
- Recommended: 1024x1024px
- Compression: 80% quality

**Profile Photos:**
- Format: JPEG/PNG
- Max size: 2MB
- Size: 400x400px
- Circle crop

### Illustrations

- Use flat design style
- Stick to primary color palette
- Include farmers and crops
- Culturally appropriate

## Error States

### Error Message Design

```
┌─────────────────────────┐
│   ⚠️ Error Title        │
│                         │
│   Clear description     │
│   of what went wrong    │
│                         │
│   [Try Again] [Cancel]  │
└─────────────────────────┘
```

**Guidelines:**
- Be clear and specific
- Suggest solutions
- Avoid technical jargon
- Provide actionable next steps

## Loading States

### Skeleton Screens

Use skeleton screens instead of spinners:
```
┌─────────────────────────┐
│  ▢▢▢▢▢▢▢▢▢▢▢▢          │
│  ▢▢▢▢▢▢▢▢▢              │
│                         │
│  ▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢      │
│  ▢▢▢▢▢▢▢▢▢▢▢▢          │
└─────────────────────────┘
```

## Multilingual Support

### Language-Specific Considerations

**Bengali (বাংলা):**
- Font: Noto Sans Bengali
- Text direction: LTR
- Line height: 1.6 (taller)

**Hindi (हिंदी):**
- Font: Noto Sans Devanagari
- Text direction: LTR
- Line height: 1.6

**Tamil (தமிழ்):**
- Font: Noto Sans Tamil
- Text direction: LTR
- Line height: 1.6

**Telugu (తెలుగు):**
- Font: Noto Sans Telugu
- Text direction: LTR
- Line height: 1.6

### Text Expansion

Allow for text expansion (30-40% for some languages):
- Flexible layouts
- Avoid fixed widths
- Test with longest language

## Dark Mode (Future)

**Color Adjustments:**
```
Background: #121212
Surface: #1E1E1E
Text: #FFFFFF (87% opacity)
Primary: #81C784 (lighter green)
```

## Performance Budget

**Target Metrics:**
- First Contentful Paint: <1.5s
- Time to Interactive: <3.5s
- Total Bundle Size: <500KB
- Images per page: <10
- API response time: <500ms

## Design Tools

**Recommended Tools:**
- Figma (UI design)
- Adobe Illustrator (icons)
- Photoshop (image editing)
- Zeplin (design handoff)

## Design Review Checklist

- [ ] Follows color palette
- [ ] Uses correct typography
- [ ] Proper spacing (8px grid)
- [ ] Accessibility compliant
- [ ] Mobile responsive
- [ ] Supports multiple languages
- [ ] Error states designed
- [ ] Loading states designed
- [ ] Icons are consistent
- [ ] Touch targets are 44x44px+

---

**Last Updated:** February 2026  
**Maintained by:** EasyAgri AI Design Team
