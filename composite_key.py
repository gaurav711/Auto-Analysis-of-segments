import pandas as pd

from pandas import Timestamp

from datetime import date, datetime

import matplotlib.pylab as plt

import matplotlib.pyplot as plt

import seaborn as sns 

names_nov =  pd.read_csv('/home/gaurav/Downloads/Nov_Dataset/Data_Nov.csv',encoding='latin')

names_dec =  pd.read_csv('/home/gaurav/Downloads/Dec_Dataset/Dataset_Dec.csv',encoding='latin')

names_jan =  pd.read_csv('/home/gaurav/Downloads/Jan_dataset/Dataset_jan.csv',encoding='latin')

names_feb =  pd.read_csv('/home/gaurav/Downloads/Feb_Dataset/Dataset_Feb.csv',encoding='latin')

names_march =  pd.read_csv('/home/gaurav/Downloads/March_reg.csv',encoding='latin')

df_list = []

df = names_dec.append(names_nov,sort=True)

df = df.append(names_jan,sort=True)

df = df.append(names_feb,sort=True)

df = df.append(names_march,sort=True)

df['date'] = pd.to_datetime(df['date'])


from datetime import date, timedelta

def foo(year, week):
    d = date(year,1,1)
    dlt = timedelta(days = (week-1)*7)
    return d + dlt

print(len(df))



num = input('Enter number of keys : ')
x2 = []
# for i in range(15):
# 		x2.append(i+1)
# print(x2)
if num == 1 :
	s1 = raw_input('first key : ')
	print(s1)
	# s1 = 'location'
	print ("type of name", type(s1)) 
	data = df.groupby(s1)[s1].count()
	print(data)
	new_df1  = pd.DataFrame({'count' : data[data>=1]}).reset_index()
	# new_df1.sort_values('count')
	final_df = new_df1.sort_values(by=['count'], ascending=False).reset_index()
	# (new_df1[s1].value_counts().to_frame().reset_index()).sort_values([s1], ascending=True)
	print(final_df)
	Total = final_df['count'].sum()
	print (Total)
	i = 0
	df1 = pd.DataFrame()
	t_cap = 0
	for index, row in final_df.iterrows() :
		if t_cap >= 60*(Total)*(1.0)/100 or row['count'] <= 0.004*(Total):
			print(row['count'])
			break

		else :
			c1 = df[df[s1]== row[s1]]
			df1 = df1.append(c1)
			t_cap = t_cap + row['count']

	from collections import OrderedDict 
	# print(len(set(df1[s1])))
	list_dict = []
	list_registration = []
	i=1
	c=0
	j = 45
	print(t_cap)
	print(len(df1))
	



	from datetime import datetime, timedelta

	while i!=0 :
		
		dw1 = df1[(df1['date'].dt.week==j)]

		if j != 45 and j!=46 and j!=47 and j!=48 :
			# start = dt - timedelta(days=dt.weekday())
			# datetime.today() - datetime.timedelta(days=datetime.today().isoweekday() % 7)
			if j > 48 :
				s11 = foo(2019,j)
				print(s11)
				x2.append(str(s11))
			else :
				s11 = (foo(2020,j))
				print(s11)
				x2.append(str(s11))
		# print(j)
		# print(dw1)
		list_registration.append(len(df[df['date'].dt.week==j]))
		j=j+1
		if j==53:
			j=1
		dff = dw1.groupby(s1)[s1].count()
		new_df2  = pd.DataFrame({'count' : dff[dff>=0]}).reset_index()
		list_dict.append(OrderedDict(sorted(new_df2.set_index(s1).T.to_dict().items())))
		c=c+1
		# print(c)
		if c==19:
			i=0	

	

	avgslopes = {}
	keys = list_dict[0].keys()
	# print(len(keys))

	list_dict_avg = {}
	for key in keys:
		av1 = 0
		for i in range(4):
			av1 = av1 + list_dict[i][key]['count']
		list_dict_avg[key] = av1*(1.0)/4
 

	for key in keys:
		m1 = 0
		
		for i in range(len(list_dict)-4) :
			m1 = m1 + ((list_dict[i+4][key]['count'] - list_dict_avg[key])*(1.0)/list_dict_avg[key])
		
			
		m1 = m1*(1.0)/15
		avgslopes[key] = m1
	# # print(avgslopes)

	

	import csv
	import collections
 
	with open('onekey.csv', 'w') as csv_file:
	    writer = csv.writer(csv_file)
	    writer.writerow(('key', 'slope'))
	    for key, value in avgslopes.items():
	    	print(key),
	    	print(value)
	        writer.writerow([key,value])
	print(avgslopes)	

	WantedOutput = sorted(avgslopes, key=lambda x : avgslopes[x])

	print(WantedOutput[0]), 

	import matplotlib.pylab as plt

	# plt.axhline(y=0.0345625213525, color='g', linestyle='-') 

	x = []
	y = []

	x.append(WantedOutput[0])
	x.append(WantedOutput[1])
	x.append(WantedOutput[2])
	x.append(WantedOutput[len(WantedOutput)-3])
	x.append(WantedOutput[len(WantedOutput)-2])
	x.append(WantedOutput[len(WantedOutput)-1])

	y.append(avgslopes[WantedOutput[0]])
	y.append(avgslopes[WantedOutput[1]])
	y.append(avgslopes[WantedOutput[2]])
	y.append(avgslopes[WantedOutput[len(WantedOutput)-3]])
	y.append(avgslopes[WantedOutput[len(WantedOutput)-2]])
	y.append(avgslopes[WantedOutput[len(WantedOutput)-1]])
	# plt.axhline(y=0.0345625213525, color='g', linestyle='-',label="Registration" + " : " + str(round(0.0345625213525,2)))
	# sort
	x1 = WantedOutput[0]
	y1 = avgslopes[WantedOutput[0]]
	colors = ['r','g','b','c','m','k','w']
	# for i in range(len(x)) :
	# 	j = i%3
	# 	plt.plot(x[i], y[i],'ro',color = colors[j],label= str(x[len(x)-i-1]) + " : " + str(round(y[len(y)-i-1],2)))
	# 	plt.legend()
	print(x)
	print(y)
	avg_reg = (len(df[(df['date'].dt.week==45)]) + len(df[(df['date'].dt.week==46)]) + len(df[(df['date'].dt.week==47)]) + len(df[(df['date'].dt.week==48)]))*(1.0)/4

	res = [(list_registration[i + 4] - avg_reg)*(1.0)/avg_reg for i in range(len(list_registration)-4)] 
	plt.plot(x2,res,marker='o',label="Registration" + " : " + str(round(0.0345625213525,2)))

	for i in range(len(x)):
		y11 = []
		jj=i
		for j in range(len(list_dict)-4):
			# ((list_dict[i+4][key]['count'] - list_dict_avg[key])*(1.0)/list_dict_avg[key])
			y11.append((list_dict[j+4][x[(len(x)-i-1)]]['count']-list_dict_avg[x[(len(x)-i-1)]])*(1.0)/list_dict_avg[x[(len(x)-i-1)]])
		
		# if x[i] == 'Kolkata' :
		# 	print("Kolkata"),
		# 	print(y11)


		# if x[i] == 'Guwahati' :
		# 	print("Guwahati"),
		# 	print(y11)

		plt.plot(x2, y11,linestyle='-',color = colors[jj],label= str(x[len(x)-i-1]) + " : " + str(round(y[len(y)-i-1],2)))
		plt.legend(loc='best')

		# print()
	plt.xlabel('Week')
	plt.ylabel('Growth')
	plt.xticks(rotation=45)

	plt.title( str(s1).title()+'\n', fontsize="15", color="green")
	plt.show()






elif num == 2 :
	s1 = raw_input('first key : ')
	s2 = raw_input('second key : ')
	data = df.groupby([s1,s2])[s1].count()
	print(data)
	new_df1  = pd.DataFrame({'count' : data[data>=1]}).reset_index()

	final_df = new_df1.sort_values(by=['count'], ascending=False).reset_index()
	# (new_df1[s1].value_counts().to_frame().reset_index()).sort_values([s1], ascending=True)
	print(final_df)
	Total = final_df['count'].sum()
	print (Total)
	i = 0
	df1 = pd.DataFrame()
	t_cap = 0
	for index, row in final_df.iterrows() :
		if t_cap >= 60*(Total)*(1.0)/100 or row['count'] <= 0.004*(Total):
			print(row['count'])
			break

		else :
			c1 = df[(df[s1]== row[s1]) & (df[s2]== row[s2]) ]
			df1 = df1.append(c1)
			t_cap = t_cap + row['count']

	from collections import OrderedDict 
	# print(len(set(df1[s1])))
	list_dict = []
	list_registration = []
	i=1
	c=0
	j = 45
	print(t_cap)
	print(len(df1))
	while i!=0 :
		
		dw1 = df1[(df1['date'].dt.week==j)]
		# print(j)
		# print(dw1)
		if j != 45 and j!=46 and j!=47 and j!=48 :
			# start = dt - timedelta(days=dt.weekday())
			# datetime.today() - datetime.timedelta(days=datetime.today().isoweekday() % 7)
			if j > 48 :
				s11 = foo(2019,j)
				print(s11)
				x2.append(str(s11))
			else :
				s11 = (foo(2020,j))
				print(s11)
				x2.append(str(s11))
		list_registration.append(len(df[df['date'].dt.week==j]))
		j=j+1
		if j==53:
			j=1
		dff = dw1.groupby([s1,s2])[s1].count()
		new_df2  = pd.DataFrame({'count' : dff[dff>=0]}).reset_index()
		list_dict.append(OrderedDict(sorted(new_df2.set_index([s1,s2]).T.to_dict().items())))
		c=c+1
		# print(c)
		if c==19:
			i=0	

	avgslopes = {}
	keys = list_dict[0].keys()
	# print(len(keys))

	list_dict_avg = {}
	for key in keys:
		av1 = 0
		for i in range(4):
			av1 = av1 + list_dict[i][key]['count']
		list_dict_avg[key] = av1*(1.0)/4


	for key in keys:
		m1 = 0
		
		for i in range(len(list_dict)-4) :
			m1 = m1 + ((list_dict[i+4][key]['count'] - list_dict_avg[key])*(1.0)/list_dict_avg[key])
		
			
		m1 = m1*(1.0)/15
		avgslopes[key] = m1
	# # print(avgslopes)
	import csv
	import collections
 
	with open('twokeys.csv', 'w') as csv_file:
	    writer = csv.writer(csv_file)
	    writer.writerow(('key', 'slope'))
	    for key, value in avgslopes.items():
	    	print(key),
	    	print(value)
	        writer.writerow([key,value])
	print(avgslopes)	

	WantedOutput = sorted(avgslopes, key=lambda x : avgslopes[x])

	print(WantedOutput[0])
	print(avgslopes[WantedOutput[0]]) 
	df_dict = pd.read_csv('twokeys.csv',encoding='latin') 

	import matplotlib.pylab as plt
 

	x = []
	y = []

	x.append(WantedOutput[0])
	x.append(WantedOutput[1])
	x.append(WantedOutput[2])
	x.append(WantedOutput[len(WantedOutput)-1])
	x.append(WantedOutput[len(WantedOutput)-2])
	x.append(WantedOutput[len(WantedOutput)-3])

	y.append(avgslopes[WantedOutput[0]])
	y.append(avgslopes[WantedOutput[1]])
	y.append(avgslopes[WantedOutput[2]])
	y.append(avgslopes[WantedOutput[len(WantedOutput)-1]])
	y.append(avgslopes[WantedOutput[len(WantedOutput)-2]])
	y.append(avgslopes[WantedOutput[len(WantedOutput)-3]])
	# plt.axhline(y=0.0345625213525, color='g', linestyle='-')
	
	print(x)
	print(y)
	colors = ['r','g','b','c','m','k','w']
	# plt.axhline(y=0.0345625213525, color='g', linestyle='-',label="Registration" + " : " + str(round(0.0345625213525,2)))
	
	# for i in range(len(x)) :
	# 		j = i%3
	# 		plt.plot(" ".join(str(x1) for x1 in x[i]), y[i],'ro',color = colors[j],label= str(" ".join(str(x1) for x1 in x[i])) + " : " + str(round(y[i],2)))
	# 		plt.legend()

	avg_reg = (len(df[(df['date'].dt.week==45)]) + len(df[(df['date'].dt.week==46)]) + len(df[(df['date'].dt.week==47)]) + len(df[(df['date'].dt.week==48)]))*(1.0)/4

	res = [(list_registration[i + 4] - avg_reg)*(1.0)/avg_reg for i in range(len(list_registration)-4)] 
	plt.plot(x2,res,marker='o',label="Registration" + " : " + str(round(0.0345625213525,2)))

	for i in range(len(x)):
			y11 = []
			jj=i
			for j in range(len(list_dict)-4):
				# ((list_dict[i+4][key]['count'] - list_dict_avg[key])*(1.0)/list_dict_avg[key])
				y11.append((list_dict[j+4][x[(len(x)-i-1)]]['count']-list_dict_avg[x[(len(x)-i-1)]])*(1.0)/list_dict_avg[x[(len(x)-i-1)]])
			

			plt.plot(x2, y11,linestyle='-',color = colors[jj],label= str(" ".join(str(x1) for x1 in x[len(x)-i-1])) + " : " + str(round(y[len(y)-i-1],2)))
			plt.legend(loc='best')
	if s1 == 'profile_segment' :
		s1 = 'profile_category'
	elif s2 == 'profile_segment':
		s2 = 'profile_category'
	plt.xlabel('weeks')
	plt.ylabel('Growth')
	plt.title( str(s1).title() + ", " + str(s2).title() + '\n', fontsize="15", color="green")
	plt.xticks(rotation=45)
	plt.show()

elif num == 3 :
	s1 = raw_input('first key : ')
	s2 = raw_input('second key : ')
	s3 = raw_input('third key : ')
	data = df.groupby([s1,s2,s3])[s1].count()
	print(data)
	new_df1  = pd.DataFrame({'count' : data[data>=1]}).reset_index()



	final_df = new_df1.sort_values(by=['count'], ascending=False).reset_index()
	# (new_df1[s1].value_counts().to_frame().reset_index()).sort_values([s1], ascending=True)
	print(final_df)
	Total = final_df['count'].sum()
	print (Total)
	i = 0
	df1 = pd.DataFrame()
	t_cap = 0
	for index, row in final_df.iterrows() :
		if t_cap >= 60*(Total)*(1.0)/100 or row['count'] <= 0.004*(Total):
			print(row['count'])
			break

		else :
			c1 = df[(df[s1]== row[s1]) & (df[s2]== row[s2]) & (df[s3]== row[s3])]
			df1 = df1.append(c1)
			t_cap = t_cap + row['count']

	from collections import OrderedDict 
	# print(len(set(df1[s1])))
	list_dict = []
	list_registration = []
	i=1
	c=0
	j = 45
	print(t_cap)
	print(len(df1))
	while i!=0 :
		
		dw1 = df1[(df1['date'].dt.week==j)]

		if j != 45 and j!=46 and j!=47 and j!=48 :
			# start = dt - timedelta(days=dt.weekday())
			# datetime.today() - datetime.timedelta(days=datetime.today().isoweekday() % 7)
			if j > 48 :
				s11 = foo(2019,j)
				print(s11)
				x2.append(str(s11))
			else :
				s11 = (foo(2020,j))
				print(s11)
				x2.append(str(s11))
				
		# print(j)
		# print(dw1)
		list_registration.append(len(df[df['date'].dt.week==j]))
		j=j+1
		if j==53:
			j=1
		dff = dw1.groupby([s1,s2,s3])[s1].count()
		new_df2  = pd.DataFrame({'count' : dff[dff>=0]}).reset_index()
		list_dict.append(OrderedDict(sorted(new_df2.set_index([s1,s2,s3]).T.to_dict().items())))
		c=c+1
		# print(c)
		if c==19:
			i=0	

	avgslopes = {}
	keys = list_dict[0].keys()
	# print(len(keys))

	list_dict_avg = {}
	for key in keys:
		av1 = 0
		for i in range(4):
			av1 = av1 + list_dict[i][key]['count']
		list_dict_avg[key] = av1*(1.0)/4

	# print(list_dict_avg)


	# y1 = 0
	# x1 = 0

	for key in keys:
		m1 = 0
		
		for i in range(len(list_dict)-4) :
			m1 = m1 + ((list_dict[i+4][key]['count'] - list_dict_avg[key])*(1.0)/list_dict_avg[key])
		
			
		m1 = m1*(1.0)/15
		avgslopes[key] = m1
	# # print(avgslopes)
	import csv
	import collections
 
	with open('threekeys.csv', 'w') as csv_file:
	    writer = csv.writer(csv_file)
	    writer.writerow(('key', 'slope'))
	    for key, value in avgslopes.items():
	    	print(key),
	    	print(value)
	        writer.writerow([key,value])
	print(avgslopes)	

	WantedOutput = sorted(avgslopes, key=lambda x : avgslopes[x])

	print(WantedOutput[0])
	print(avgslopes[WantedOutput[0]]) 
	 

	import matplotlib.pylab as plt

	 
	x = []
	y = []

	x.append(WantedOutput[0])
	x.append(WantedOutput[1])
	x.append(WantedOutput[2])
	x.append(WantedOutput[len(WantedOutput)-3])
	x.append(WantedOutput[len(WantedOutput)-2])
	x.append(WantedOutput[len(WantedOutput)-1])

	y.append(round(avgslopes[WantedOutput[0]],2))
	y.append(round(avgslopes[WantedOutput[1]],2))
	y.append(round(avgslopes[WantedOutput[2]],2))
	y.append(round(avgslopes[WantedOutput[len(WantedOutput)-3]],2))
	y.append(round(avgslopes[WantedOutput[len(WantedOutput)-2]],2))
	y.append(round(avgslopes[WantedOutput[len(WantedOutput)-1]],2))
	 

	print(x)
	print(y)

	import numpy as np

	# x2 = np.linspace(0, 1, 10)
	# number = 5
	fig, ax = plt.subplots()
	# cmap = plt.get_cmap('gnuplot')
	# colors = [cmap(i) for i in np.linspace(0, 1, number)]
	colors = ['r','g','b','c','m','k','w']
	# ax.set_prop_cycle(['red', 'black', 'yellow'])
	# cm = ax.get_cmap('gist_rainbow')
	# fig = plt.figure()
	# ax = fig.add_subplot(111)
	# ax.set_prop_cycle('color', ['r','g','b'])
	# ax.axhline(y=0.0345625213525, color='g', linestyle='-',label="Registration" + " : " + str(round(0.0345625213525,2)))
	
	# for i in range(len(x)) :
	# 		j = i%3
	# 		# print(j)
	# 		# print(colors[j])
	# 		ax.plot(" ".join(str(x1) for x1 in x[i]), y[i],'ro',color = colors[j],label= str(" ".join(str(x1) for x1 in x[i])) + " : " + str(round(y[i],2)))
	# 		ax.legend(loc='best')

	avg_reg = (len(df[(df['date'].dt.week==45)]) + len(df[(df['date'].dt.week==46)]) + len(df[(df['date'].dt.week==47)]) + len(df[(df['date'].dt.week==48)]))*(1.0)/4

	res = [(list_registration[i + 4] - avg_reg)*(1.0)/avg_reg for i in range(len(list_registration)-4)] 
	plt.plot(x2,res,marker='o',label="Registration" + " : " + str(round(0.0345625213525,2)))


	for i in range(len(x)):
				y11 = []
				jj=i
				for j in range(len(list_dict)-4):
					# ((list_dict[i+4][key]['count'] - list_dict_avg[key])*(1.0)/list_dict_avg[key])
					y11.append((list_dict[j+4][x[(len(x)-i-1)]]['count']-list_dict_avg[x[(len(x)-i-1)]])*(1.0)/list_dict_avg[x[(len(x)-i-1)]])
				

				plt.plot(x2, y11,linestyle='-',color = colors[jj],label= str(" ".join(str(x1) for x1 in x[len(x)-i-1])) + " : " + str(round(y[len(y)-i-1],2)))
				plt.legend(loc='best')

	plt.xlabel('Segment')
	plt.ylabel('Growth')
	if s1 == 'profile_segment' :
		s1 = 'profile_category'
	elif s2 == 'profile_segment':
		s2 = 'profile_category'
	elif s3 == 'profile_segment':
		s3 = 'profile_category'

	plt.title( str(s1).title() +", "+str(s2).title() +", "+ str(s3).title() + '\n', fontsize="15", color="green")
	plt.xticks(rotation=45)
	plt.show()
# 
# data = df.groupby(['location','profile_flag','industry']).profile_flag.count()




# print(data)
# new_df1  = pd.DataFrame({'count' : data[data>=1]}).reset_index()
# new_df1.to_csv('file_name5_profile_segment_30.csv',encoding='utf-8')

# print(len(new_df1))

# avg =0.0
# sd = 0.0
# for index, row in new_df1.iterrows():
# 	avg = avg + row['count']
# print(avg)

# avg = avg*(1.0)/922
# print(avg)

# for index, row in new_df1.iterrows():
# 	sd = sd + (row['count']-avg)**(2)

# sd = sd*(1.0)/922
# print(sd**(0.5))
# c1 = pd.DataFrame()

# for index, row in new_df1.iterrows():
# 	# print(row['location'],row['industry'],row['profile_flag'],row['count'])
# 	c1 = c1.append(df[(df['profile_segment']==row['profile_segment']) & (df['profile_flag'] == row['profile_flag'])&  (df['industry'] == row['industry'])])

# c1.to_csv('file_name5_ps.csv',encoding='utf-8')
# print(len(c1))
# df1= c1
# print(len(c1))
# from collections import OrderedDict 
 
# list_dict = []
# list_registration = []
# i=1
# c=0
# j = 45
# while i!=0 :
	
# 	dw1 = df1[(df1['date'].dt.week==j)]
# # 	# print(j)
# # 	# print(dw1)
# 	list_registration.append(len(df[df['date'].dt.week==j]))
# 	j=j+1
# 	if j==53:
# 		j=1
# 	dff = dw1.groupby(['profile_segment','profile_flag','industry']).profile_flag.count()
# 	new_df1  = pd.DataFrame({'count' : dff[dff>=0]}).reset_index()
# 	list_dict.append(OrderedDict(sorted(new_df1.set_index(['profile_segment','profile_flag','industry']).T.to_dict().items())))
# 	c=c+1
# 	# print(c)
# 	if c==19:
# 		i=0

# # print(len(list_dict[0]))
# # # print(list_dict[0])
# # print(list_registration)
# # # for i in range(19):
# # # 	print((list_dict[i]))
# # # # print(list_dict[1])
# # # # print(list_dict[2])
# # m = 0
# # m_x = 0
# # for i in range(len(list_registration)):
# # 	m = m + list_registration[i]
# # 	# m_x = (m + (list_registration[i])**(2)
# # print(m)
# # # print(m_x)
# # print('*****')

# # m = m*(1.0)/19
# # # m_x = m_x*(1.0)/19
# # print(m)
# # m_x  = 0.0
# # for i in range(len(list_registration)):
# # 	m_x = m_x + (list_registration[i]-m)**2
# # m_x = m_x*(1.0)/19
# # print(m_x**(0.5))

# # # print('*****')
# # # print(m_x)
# # # print('*****')
# # # sd = (m_x - m)**(0.5)

# # # print(sd) 

# avgslopes = {}
# keys = list_dict[0].keys()

# # # for key in keys :
# # # 	print(key)
# # 	print(list_dict[0][key]['count'])

# print(list_dict[0]['Bangalore/Bengaluru','y','IT-Software/Software Services']['count'])
# # print(keys)
# # print(k2)

# list_dict_avg = {}
# for key in keys:
# 	av1 = 0
# 	for i in range(4):
# 		av1 = av1 + list_dict[i][key]['count']
# 	list_dict_avg[key] = av1*(1.0)/4

# # print(len(list_dict_avg))


# for key in keys:
# 	m1 = 0
# 	for i in range(len(list_dict)-4) :
# 		m1 = m1 + ((list_dict[i+4][key]['count'] - list_dict_avg[key])*(1.0)/list_dict_avg[key])
# 	m1 = m1*(1.0)/15
# 	avgslopes[key] = m1
# print(avgslopes)


# import matplotlib.pylab as plt

# plt.axhline(y=0.0345625213525, color='g', linestyle='-')
# lists = sorted(avgslopes.items()) # sorted by key, return a list of tuples

# print(lists)
# x, y = zip(*lists) # unpack a list of pairs into two tuples
# print(x)
# print(y)
# # x = avgslopes.keys()
# # y = []
# # for i in range(112):
# # 	y.append
# # x = hash(tuple(x.array([1,2,3])))
# # plt.plot(x, y,'ro')
# # plt.show()
