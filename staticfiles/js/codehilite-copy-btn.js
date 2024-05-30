document.addEventListener('DOMContentLoaded', () => {
  // Function to copy text from a code element
  function copyCodeText(codeElement, button) {
    const textToCopy = codeElement.textContent;
    navigator.clipboard.writeText(textToCopy).then(() => {
      // Change button text to "Copied!"
      button.innerText = 'Copied!';
      // Change button text back to "Copy Code" after 3 seconds
      setTimeout(() => {
        button.innerText = 'Copy Code';
      }, 3000);
    }).catch(err => {
      console.error('Failed to copy text: ', err);
    });
  }

  // Find all elements with the class 'codehilite'
  const codehiliteElements = document.querySelectorAll('.codehilite');

  codehiliteElements.forEach(codehilite => {
    // Create a button element
    const copyButton = document.createElement('button');
    copyButton.innerText = 'Copy Code';

    // Add classes to the button
    copyButton.classList.add('btn', 'btn-secondary', 'mb-2');

    // Add click event listener to the button
    copyButton.addEventListener('click', (event) => {
      const codeElement = codehilite.querySelector('code');
      if (codeElement) {
        // Pass the specific button that was clicked
        copyCodeText(codeElement, event.currentTarget);
      } else {
        console.error('No <code> element found within .codehilite');
      }
    });

    // Insert the button right after the 'codehilite' element
    codehilite.parentNode.insertBefore(copyButton, codehilite.nextSibling);
  });
});

