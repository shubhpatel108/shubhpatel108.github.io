images = [
	["gdg_summit.jpg", "GDG India Summit 2015"],
	["gdg15.jpg", "Google Developer Group, DA-IICT"],
	["wtm.jpg", "Women Techmakers India Summit, 2016"],
	["google_android_certification.jpg", "Google Android Certification Summit 2017"],
	["gdg_devfest_cmb.jpg", "Speaking at Google Developer Group DevFest, Coimbatore, 2017"],
	["un_xprize.jpg", "Xprize Women Safety and Water Safety Launch, United Nations"],
	["rural.jpg", "Rural Internship, 2013"],
	["kde.jpg", "KDE Summit, 2014"],
];

BASE_URL = "gallery/"

def getHTML(pic1, pic2):
    return '<div class="row">' + \
		pic1 + pic2 + \
    '</div>'

def getPicHTML(image_id, image_url, caption):
	html = '<div class="col-md-6">' + \
        '<a class="lightbox" href="#' + image_id + '">' + \
        	'<img src="' + image_url + '"/>' + \
        '</a>' + \
        '<p>' + caption + '</p>' + \
  	'</div>';

  	return html;

def getZoomHTML(image_id, image_url):
	return '<div class="lightbox-target" id="' + image_id + '">' + \
	  	'<img src="' + image_url + '"/>' + \
	   	'<a class="lightbox-close" href="#"></a>' + \
	'</div>'

def generate():
	for first, second in zip(images, images[1:])[::2]:
		pic1 = getPicHTML(first[0].split(".")[0], BASE_URL + first[0], first[1]);		
		pic2 = getPicHTML(second[0].split(".")[0], BASE_URL + second[0], second[1]);		
		print getHTML(pic1, pic2)

def generateZoom():
	for image in images:
		print getZoomHTML(image[0].split(".")[0], BASE_URL + image[0])

generateZoom();