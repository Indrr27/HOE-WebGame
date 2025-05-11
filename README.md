# hoe.love – A Love2D Web Game

**hoe.love** is a pixel-art style 2D web game built with [LÖVE](https://love2d.org/) and compiled to WebAssembly using [love.js](https://github.com/Davidobot/love.js). The game runs directly in the browser and features animated characters, background effects, and interactive UI elements.

## 🚀 Live Demo

Check out the game here: [https://your-netlify-link.netlify.app](https://hoegame.netlify.app/)

## 🎮 Features

- ✅ Love2D engine exported for the web using Emscripten
- ✅ Background canvas animation with smooth scaling
- ✅ Walking sprite with idle transitions
- ✅ Responsive design that scales properly with window size

## 📁 Project Structure
hoe-love/
├── index.html              # Main HTML entry point
├── game.js                 # Compiled Love2D project (via love.js)
├── love.js                 # JavaScript runtime for LÖVE
├── game.love               # Zipped LÖVE game source
├── theme/
│   ├── love.css            # Custom stylesheet
│   ├── frame.png           # Background frame image
│   ├── eoe.png             # Floating button in the corner
│   ├── gal1sideways*.png   # Walking animation frames
│   ├── gal1idle*.png       # Idle animation frames
├── _headers (optional)     # CORS headers for Netlify
