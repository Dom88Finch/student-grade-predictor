

import tkinter as tk 
import math
import pickle


HEIGHT = 700
WIDTH = 800





def format_response(prediction):

	prediction= str(prediction)[2:-2]
	#print(prediction)
	prediction_1 = round(float(prediction),2)
	#print(prediction_1)

	try:
		final_prediction= 'Student grade prediction:%s ' %(prediction_1)
	except:
		final_prediction = 'There was a problem \n predicting your student outcome'

	return final_prediction


def our_predictor(entry,entry_2,entry_3,entry_4,entry_5):
	
	if entry_5 == "M":
		gender = 0
	else:
		gender =1
	print('ubiubiubui',gender)
	pickle_in = open("studentmodel_new.pickle", "rb")
	#m = [int(entry),int(entry_2)]
	m = [int(entry),int(entry_2),int(entry_3), int(entry_4),gender]
	# load our saved model 
	linear = pickle.load(pickle_in)
	#entry=np.array(entry)
	print(m)
	prediction = linear.predict([m])
	print(prediction)

	label['text'] = format_response(prediction)


root = tk.Tk()


canvas = tk.Canvas(root, bg="gray", height=HEIGHT, width=WIDTH)
canvas.pack()


background_image = tk.PhotoImage(file='exam_background.png') # make sure the image is 'PNG' and not 'JPEG'
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)





frame = tk.Frame(root, bg='white', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1,anchor='n')

ovrl_descr = tk.Label(frame, text= 'fill in the data below and then press predict \nto use machine learning to predict\n the grade of third term',bg='green',font=('Rockwell Extra Bold', 10))
ovrl_descr.place(relwidth=0.65, relheight=1 )





frame_2 = tk.Frame(root, bg='gray', bd=5)
frame_2.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.4,anchor='n')



#feature grade_1
entry = tk.Entry(frame_2, bg='gray',font=('Rockwell Extra Bold', 20))
entry.grid(row=0,column=2)

desc = tk.Label(frame_2, text=' enter grade 1 [0-19]',font=('Arial', 14))
desc.grid(row=0,column=1)



#feature grade_2
entry_2 = tk.Entry(frame_2, bg='gray',font=('Rockwell Extra Bold', 20))
entry_2.grid(row=1,column=2)

desc_2 = tk.Label(frame_2, text=' enter grade 2 [0- 19]',font=('Arial', 14))
desc_2.grid(row=1,column=1)

# feature study_time
entry_3 = tk.Entry(frame_2, bg='gray',font=('Rockwell Extra Bold', 20))
entry_3.grid(row=2,column=2)


desc_3 = tk.Label(frame_2, text=' Study time (hours per_day: [1-4]',font=('Arial', 14))
desc_3.grid(row=2,column=1)

entry_4 = tk.Entry(frame_2, bg='gray',font=('Rockwell Extra Bold', 20))
entry_4.grid(row=3,column=2)

desc_4 = tk.Label(frame_2, text='age ([15-22]',font=('Arial', 14))
desc_4.grid(row=3,column=1)




entry_5 = tk.Entry(frame_2, bg='gray',font=('Rockwell Extra Bold', 20))
entry_5.grid(row=4,column=2)

desc_5 = tk.Label(frame_2, text='gender [M or F]',font=('Arial', 14))
desc_5.grid(row=4,column=1)




# C1 = Checkbutton(frame_2, text = "Male", variable = CheckVar1, \
#                  onvalue = 1, offvalue = 0, height=5, \
#                  width = 20)

# C2 = Checkbutton(frame_2, text = "Female", variable = CheckVar2, \
#                  onvalue = 1, offvalue = 0, height=5, \
#                  width = 20)


# C1.grid(row=3,column=3)
# C2.grid(row=3,column=3)





button =tk.Button(frame,text='Predict',bg='gray',font=('Copperplate Gothic Bold', 10),
					command=lambda: our_predictor(entry.get(),
						entry_2.get(),entry_3.get(),entry_4.get(),entry_5.get()))

button.place(relx=0.7,  relwidth=0.3, relheight=1)



frame_b = tk.Frame(root,bg='#80c1ff',bd= 10)
frame_b.place(relx=0.5, rely= 0.5, relwidth=0.75,relheight=0.2, anchor='n' )


label = tk.Label(frame_b, bg='green', font=('Rockwell Extra Bold', 12), anchor='nw', justify='left', bd=5)
label.place(relwidth=1, relheight=1)




root.mainloop()

