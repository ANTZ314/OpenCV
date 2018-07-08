# Image Scrapers
---------

#### Create Dataset from Bing with API:
* [Bing]()

#### Create Dataset from Manual Capture:
* [Capture](https://www.pyimagesearch.com/2018/06/11/how-to-build-a-custom-face-recognition-dataset/)


#### Create Dataset from Google Images:  
* [google](https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/)

**Notes:**  

* Open Google Images and run custome search
* The next step is to use JavaScript to gather the image URLs
* In Chrome: **Top Right => More Tools ==> Developer Tools**
* Select Java Console (allows to run the Java Script)
* Sroll as far down as is needed for images to generate
* Now copy and paste the following sections into the console and run:

First:

	    // pull down jquery into the JavaScript console
    	var script = document.createElement('script');
    	script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js";
    	document.getElementsByTagName('head')[0].appendChild(script);
Next:        

      	// grab the URLs
		var urls = $('.rg_di .rg_meta').map(function() { return JSON.parse($(this).text()).ou; });
        
Finally:

		// write the URls to file (one per line)
		var textToSave = urls.toArray().join('\n');
		var hiddenElement = document.createElement('a');
		hiddenElement.href = 'data:attachment/text,' + encodeURI(textToSave);
		hiddenElement.target = '_blank';
		hiddenElement.download = 'urls.txt';
		hiddenElement.click();
        
* Then move the stored "URL.txt" file to the working folder
* Now with the URL list in the working folder, run the Python Script
