def create_youtube_video(title,description)
  	video = {"title"=title,"description"=description,likes=0,dislikes=0,comments={comment=""}}

def like(video)
	video[likes]+=1

def dislikes(video)
	video[dislikes]+=1

def add_comment(video,username,comment_text)
	