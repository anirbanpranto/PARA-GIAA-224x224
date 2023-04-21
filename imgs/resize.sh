for i in {1..446}
do
   	exec "mogrify -resize 224x224! *.jpg"
	exec "cd.."
done
