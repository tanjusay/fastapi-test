from pytailwindcss import TailwindCSS

# Initialize the TailwindCSS compiler
tailwind = TailwindCSS(input_css='./static/css/styles.css', output_css='./static/css/output.css')

# Compile the CSS
tailwind.compile()
