# from pytube import YouTube

# def downloader(url, output_path='.'):
#     try:
#         yt = YouTube(url)
#         stream = yt.streams.get_highest_resolution()
#         stream.download(output_path) 

#         print(f"Downloaded: {yt.title}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# video_url = input("Enter the YouTube video URL: ")
# output_path = input("Enter the output path (leave blank for current directory): ")

# if not output_path:
#     output_path = '.' 

# downloader(video_url, output_path) 

from pytube import YouTube

def downloader(url, output_path='.'):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True) 
        for i, stream in enumerate(streams):
            print(f"{i}. {stream}")
        
        choice = int(input("Enter the number of the stream to download: "))
        selected_stream = streams[choice]

        selected_stream.download(output_path)
        print(f"Downloaded: {yt.title}")

    except Exception as e:
        print(f"An error occurred: {e}")

video_url = input("Enter the YouTube video URL: ")
output_path = input("Enter the output path (leave blank for current directory): ")

if not output_path:
    output_path = '.' 

downloader(video_url, output_path) 