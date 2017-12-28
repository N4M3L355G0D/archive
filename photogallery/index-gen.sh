#! /bin/bash


firsthalf() {
cat << EOF

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<title>Simple HTML Photo Gallery with JavaScript</title>

<style type="text/css">
body {
        background: #222;
        color: #eee;
        margin-top: 20px;
        font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
}
a {
        color: #FFF;
}
a:hover {
        color: yellow;
        text-decoration: underline;
}
.thumbnails img {
        height: 80px;
        border: 4px solid #555;
        padding: 1px;
        margin: 0 10px 10px 0;
}

.thumbnails img:hover {
        border: 4px solid #00ccff;
        cursor:pointer;
}

.preview img {
        border: 4px solid #444;
        padding: 1px;
        width: 800px;
}
</style>

</head>
<body>

<div class="gallery" align="center" >
        <h2>B.A.S. Storage Server </h2>
        <p>Created with a code Hybrid from <a target="_blank" href="http://html-tuts.com/">HTML-TUTS.com</a> and Ni64 Systems, inc. View the full tutorial that generated the code for this page's generation, <a href="http://html-tuts.com/?p=2337" target="_blank">here</a>.</p>

        <br />

        <div class="thumbnails" style="width: 1000px; max-height: 100px ;  border:1px solid gray ; overflow-y:scroll">

EOF
}

template() {

cat << EOF

<img onmouseover="preview.src=img1.src" name="img1" src="images/img1.jpg" alt=""/>
                <img onmouseover="preview.src=img2.src" name="img2" src="images/img2.jpg" alt=""/>
                <img onmouseover="preview.src=img3.src" name="img3" src="images/img3.jpg" alt=""/>
                <img onmouseover="preview.src=img4.src" name="img4" src="images/img4.jpg" alt=""/>
                <img onmouseover="preview.src=img5.src" name="img5" src="images/img5.jpg" alt=""/>

EOF

}

lasthalf() {

cat << EOF

</div><br/>

        <div class="preview" align="center">
                <img name="preview" src="pictures/manjaro.jpg" alt=""/>
        </div>

</div>


</body>
</html>


EOF

}

firsthalf
bash finder.sh
lasthalf
