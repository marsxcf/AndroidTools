<?php 
	$ZIP_SHORT = 2;
	$MAGIC = '!ZXK!';
	$path = "app-release.apk";
	$comment = "channel_2743_5556";
	$fp = fopen($path , 'r+');
	fseek($fp, -$ZIP_SHORT, SEEK_END); 
	fwrite($fp, pack('v', strlen($comment) + $ZIP_SHORT + strlen($MAGIC)));
	fwrite($fp, $comment);
	fwrite($fp, pack('v', strlen($comment)));
	fwrite($fp, $MAGIC);
	fclose($fp);

	$zip = new ZipArchive();
	$zip->open($path);
	echo $zip->getArchiveComment();
?>