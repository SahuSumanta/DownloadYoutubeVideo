from pytube import YouTube


link = input("Enter the YouTube Link : ")
yt = YouTube(link)

videos = yt.streams.all()
i = 1

#it used for user convinience
for streams in videos:
    print(str(i) + " " +str(streams))
    i += 1

stream_number = int(input("enter number : "))
#for the user convienience because user don't no programm start from zero.
video = videos[stream_number - 1]

#D:\Movies is the path you can give otherwise it's okay.
video.download("D:\Movies")
#When you have sucessfully download it.
print("downloaded")