
# from moviepy.editor import *

# # 创建文本剪辑
# text_clip_1 = TextClip("Hey there!", fontsize=70, color='black', bg_color='white').set_position(('center', 'top'))
# text_clip_2 = TextClip("My name is Yiren.", fontsize=70, color='black', bg_color='white').set_position(('center', 'bottom'))

# # 给文本剪辑添加动效
# text_clip_1 = text_clip_1.set_duration(3).crossfadein(0.5).crossfadeout(0.5)
# text_clip_2 = text_clip_2.set_duration(3).crossfadein(0.5).crossfadeout(0.5)

# # 将文本剪辑合成一个视频剪辑
# video_clip = CompositeVideoClip([text_clip_1, text_clip_2], size=(600, 400)).set_duration(6)

# # 将视频剪辑导出为 GIF
# video_clip.write_gif("my_text_effect.gif", fps=10)

from moviepy.editor import *

# 创建文本剪辑
# text_clip_1 = TextClip("Hey there!", fontsize=70, color='black', bg_color='white').set_position(('center', 'top'))
# text_clip_2 = TextClip("My name is Yiren.", fontsize=70, color='black', bg_color='white').set_position(('center', 'bottom'))
# background = ColorClip(size=(1920, 1080), color=(255, 255, 255), duration=6)
background = ColorClip(size=(800, 600), color=(12, 14, 18), duration=6)
# background = ColorClip(size=(800, 600), color=(255, 255, 255), duration=6)
# font= "HelveticaNeue"
font = "Times"
fontsize = 60
text = "Hey there!\nWelcome to my Github."
fps = 8
bg_color = "#0C0E12"
# bg_color = "white"
duration = len(text) / fps
text_clip_1 = TextClip(" ", font=font, fontsize=fontsize, color='#DA7885', bg_color=bg_color).set_position(('center', 'center'))

# 给文本剪辑添加动效
text_clip_1 = text_clip_1.set_duration(duration).crossfadein(0.5).crossfadeout(0.5)

# text_clip_1 = CompositeVideoClip([background, text_clip_1], size=(800, 600)).set_duration(6)
idx = 999
# text_clip_2 = text_clip_2.set_duration(3).crossfadein(0.5).crossfadeout(0.5)
for i in range(len(text)):
    if (text[i] == "W"):
        idx = i
    if i>=idx:
        text_clip_i = TextClip(text[:i+1],font=font, fontsize=fontsize, color='#DA7885', bg_color=bg_color).set_position(('center', 'center'))
    else:
        text_clip_i = TextClip(text[:i+1], font=font, fontsize=fontsize, color='#DA7885', bg_color=bg_color).set_position(('center', 'center'))
    text_clip_i = text_clip_i.set_start(i / fps)
    text_clip_i = text_clip_i.set_duration(1 / fps)
    text_clip_1 = CompositeVideoClip([background,text_clip_1, text_clip_i], size=(800, 600)).set_duration(6)

# text = "My name is Yiren."
# fps = 5
# duration = len(text) / fps
# text_clip_2 = TextClip(" ", fontsize=60, color='black', bg_color='white').set_position(('center', 'bottom'))

# # 给文本剪辑添加动效
# text_clip_2 = text_clip_2.set_duration(duration).crossfadein(0.5).crossfadeout(0.5)

# text_clip_2 = CompositeVideoClip([text_clip_1, text_clip_2], size=(600, 400)).set_duration(6)

# # text_clip_2 = text_clip_2.set_duration(3).crossfadein(0.5).crossfadeout(0.5)
# for i in range(len(text)):
#     text_clip_i = TextClip(text[:i+1], fontsize=60, color='black', bg_color='white').set_position(('center', 'bottom'))
#     text_clip_i = text_clip_i.set_start(i / fps)
#     text_clip_i = text_clip_i.set_duration(1 / fps)
#     text_clip_2 = CompositeVideoClip([text_clip_2, text_clip_i], size=(600, 400)).set_duration(6)

# 将文本剪辑合成一个视频剪辑
# video_clip = CompositeVideoClip([text_clip_1, text_clip_2], size=(600, 400)).set_duration(6)

# 将视频剪辑导出为 GIF
text_clip_1.write_gif("my_text_effect11.gif", fps=fps)