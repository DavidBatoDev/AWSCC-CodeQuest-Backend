/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./main/templates/*"],
  theme: {
    extend: {},
  },
  plugins: [],
}

// npx tailwindcss -i ./main/static/src/input.css -o ./main/static/css/main.css --watch
