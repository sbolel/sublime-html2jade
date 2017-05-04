# HTML to JADE plugin for Sublime Text 3

Converts files, selection and clipboard content from HTML to JADE using html2jade

## Installation

### [Sublime Package Control](http://wbond.net/sublime_packages/package_control)

In the command Pallette choose **Package Control: Add Repository** and enter the Github URL:

    https://github.com/sbolel/sublime3-html2jade

Then choose **Package Control: Install Package** and select sublime-html2jade to install.

Install *html2jade*:

    npm install -g html2jade

On OSX sublime text does not use the same path as your shell, you might need to install the
"Fix Mac Path" package via Package Control.

### Git installation

Clone the repository in your Sublime Text "Packages" directory:

    git clone https://github.com/sbolel/sublime3-html2jade.git Html2Jade

Install *html2jade*:

    npm install -g html2jade

The "Packages" directory is located at:

* OS X:

        ~/Library/Application Support/Sublime Text 3/Packages/

* Linux:

        ~/.config/sublime-text-3/Packages/

* Windows:

        %APPDATA%/Sublime Text 3/Packages/

## Usage

* **Convert whole HTML file** `Shift+Alt+F` - creates new file in the same folder using the same name as the source ending with '.html'.
* **Convert selection** `Shift+Alt+S` - replaces selection of HTML with JADE content.
* **Convert clipboard content** `Shift+Alt+V` - inserts JADE of converted clipboard HTML content.

### In Command Palette:

* **HTML2Jade: Convert file**
* **HTML2Jade: Convert selection**
* **HTML2Jade: Convert clipboard content**

## Sublime Text 2

Follow the instruction from [Sublime Text 2 branch](https://github.com/anderson916/sublime-html2jade/tree/SublimeText2)
