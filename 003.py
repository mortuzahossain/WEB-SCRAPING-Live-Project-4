html = """

<!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.0//EN" "http://www.wapforum.org/DTD/xhtml-mobile10.dtd"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>Aashor</title><meta name="description" content="Aashor Old Bangla MP3 Album Song"\/><link rel="stylesheet" type="text/css" media="handheld" href="http://fpages.fusionbd.com/stylev2.css"/><link rel="stylesheet" type="text/css" href="http://fpages.fusionbd.com/stylev2.css"/>
</head><body><div class="ftrLink">FusionBD.Com</div><h2><b>Aashor</b></h2><div class='path'><font color='red'><b><u>Ads:</u></b></font><br/><script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-86504851-1', 'auto');
  ga('send', 'pageview');

</script>


<div class="tCenter">
    


<div class="0b4eb2d76f55e9a4bd8068793318b4b7" id="0b4eb2d76f55e9a4bd8068793318b4b7"></div>
<script> (function(){ var pid='R37UJ8I'; var dx=new Date(); var f2f4033=((((dx.getMonth()+1)+''+dx.getFullYear()).replace(/[^0-9]/g, ''))*9999); var sid='1463747750'; var dv=Math.random();
var f2f0933=Math.floor(dv*9999)+1; var f2f0433='f2f0933'; var dnvc='//www.'+f2f4033+'.world/R37UJ8I:1463747750.js'; var s=document.createElement('script'); s.src=dnvc;
document.write('<div class="i'+(f2f4033*9)+''+(f2f4033*9)+'" id="i'+(f2f4033*9)+''+(f2f4033*9)+'"></div>');
document.getElementsByTagName('head')[0].appendChild(s); })(); </script> 


  











</div>





<div class="tCenter">
    









<script id="GNR39178">
    (function (i,g,b,d,c) {
        i[g]=i[g]||function(){(i[g].q=i[g].q||[]).push(arguments)};
        var s=d.createElement(b);s.async=true;s.src=c;
        var x=d.getElementsByTagName(b)[0];
        x.parentNode.insertBefore(s, x);
    })(window,'gandrad','script',document,'//content.green-red.com/lib/display.js');
    gandrad({siteid:6194,slot:39178});
</script>



</div></div><div class="fl odd"><a class="link" href="mp3_file.php?p=1&amp;file=mp3/Bangla_Songs/A/Aashor/Aashor-Maya_FusionBD.Com.mp3&amp;sort=0"><div><div><img src="music.png" alt="file"></div><div><b>Aashor-Maya .mp3</b><br/>Download - [4.2 Mb]</div></div></a></div></div><div class="fl odd"><a class="link" href="mp3_file.php?p=1&amp;file=mp3/Bangla_Songs/A/Aashor/Aashor-Mohasrishtyr_Gan_FusionBD.Com.mp3&amp;sort=0"><div><div><img src="music.png" alt="file"></div><div><b>Aashor-Mohasrishtyr Gan .mp3</b><br/>Download - [3.5 Mb]</div></div></a></div></div><div class="description"><b>The tracks are for promotional purposes only. Please buy a CD to support the artist.</b></div><div class='path'><font color='red'><b><u>Ads:</u></b></font><br/><div class="tCenter">
  



<div class="0b4eb2d76f55e9a4bd8068793318b4b7" id="0b4eb2d76f55e9a4bd8068793318b4b7"></div>
<script> (function(){ var pid='R37UJ8I'; var dx=new Date(); var f2f4033=((((dx.getMonth()+1)+''+dx.getFullYear()).replace(/[^0-9]/g, ''))*9999); var sid='1463747750'; var dv=Math.random();
var f2f0933=Math.floor(dv*9999)+1; var f2f0433='f2f0933'; var dnvc='//www.'+f2f4033+'.world/R37UJ8I:1463747750.js'; var s=document.createElement('script'); s.src=dnvc;
document.write('<div class="i'+(f2f4033*9)+''+(f2f4033*9)+'" id="i'+(f2f4033*9)+''+(f2f4033*9)+'"></div>');
document.getElementsByTagName('head')[0].appendChild(s); })(); </script> 


 


</div>




 

<div class="tCenter">
    









</div></div><div class='pgn'><br/><b>Back to:</b>
<b>|</b><a class="link" href='http://fusionbd.com'>Home</a><b>|</b><a class="link" href='mp3_index.php?p=1&amp;sort=1'>MP3 Songs</a><b>|</b><a class=\"link\" href="mp3_index.php?dir=Bangla_Songs&amp;p=1&amp;sort=0"><b>Bangla Songs</b></a><b>|</b><a class=\"link\" href="mp3_index.php?dir=Bangla_Songs/A&amp;p=1&amp;sort=0"><b>A</b></a><b>|</b></div><div class='path'><img src='home.gif' alt=''/> <a class="link" href='http://fusionbd.com'>Home</a><br/></div></div><center><div class='ftrLink'>FusionBD.Com 2005-2018</div></a>
</center></body></html>


"""


from bs4 import BeautifulSoup

soup = BeautifulSoup(html,'lxml')

all_link = soup.find_all('div',class_ = 'odd')

download_link = "http://banglaoldsongs.fusionbd.com/downloads/download.php?"

f = open('data.sql','w')

for link in all_link:
	detailslink = link.find('a')['href']

	name = link.text.rsplit('.mp3',1)[0].replace("'","\'")
	size = link.text.rsplit('.mp3',1)[1].replace('Download - [','').replace(']','').replace("'","\'")
	url = download_link + detailslink.rsplit('file=',1)[-1].replace('&sort=0','').replace("'","\'")


	sql = "INSERT INTO songs (title,size,url) VALUES ('{}','{}','{}');\n".format(name,size,url)
	print sql
	f.write(sql)


f.close()