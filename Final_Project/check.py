import pymysql
import sys
import io
import time
from sklearn.externals import joblib
import pandas as pd
import datetime
import math

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
class search:

	def __init__(self, id = None, fleetName = None):
		self.id = str(id)
		self.fleetName = str(fleetName)
		self.per_page = 50

	def connect(self):
		db = pymysql.connect(
			host = '134.175.31.246',
			port = 3306,
			user = 'Jimmy',
			passwd = 'PPfrog@0519',
  			database = 'Data')
 
		cursor = db.cursor()
		return cursor, db

	def check_plane_type(self, cursor):				## check if the id is in the database, if true return the table name, if false return false
		try:
			sql = "SELECT * FROM 787_FLIGHT where AC= \"" + self.id + "\" "
			cursor.execute(sql)
			results = cursor.fetchall()
			a = results[0][0]
			return "787_FLIGHT"
		except IndexError:
			pass
		try:
			sql = "SELECT * FROM 737_FLIGHT where AC= \"" + self.id + "\" "
			cursor.execute(sql)
			results = cursor.fetchall()
			a = results[0][0]
			return "737_FLIGHT"
		except IndexError:
			pass

		try:
			sql = "SELECT * FROM 757_FLIGHT where AC= \"" + self.id + "\" "
			cursor.execute(sql)
			results = cursor.fetchall()
			a = results[0][0]
			return "757_FLIGHT"
		except IndexError:
			return False

		
	def check_exist(self):				## check if the plane exist, return true or false
		cursor, db = self.connect()
		result = self.check_plane_type(cursor)
		db.close()
		if result == False:
			return False
		else:
			return True

	def find_all_plane_helper(self, cursor):
		if self.fleetName == "787-8": 
			sql_1 = "SELECT distinct AC FROM 787_FLIGHT "
			cursor.execute(sql_1)
			results_787 = cursor.fetchall()
		# 	list_787 = []
		# 	for a in range((results_787.__len__())):
		# 		list_787.append("AC" + results_787[a][0])
			return results_787
		if self.fleetName == "757-200": 
			sql_2 = "SELECT distinct AC FROM 757_FLIGHT"
			cursor.execute(sql_2)
			results_757 = cursor.fetchall()
			# list_757 = []
			# for a in range((results_757.__len__() - 1)):
			# 	list_757.append("AC" + results_757[a][0])
			return results_757

		if self.fleetName == "737-800":
			sql_3 = "SELECT distinct AC FROM 737_FLIGHT"
			cursor.execute(sql_3)
			results_737 = cursor.fetchall()
			# list_737 = []
			# for a in range((results_737.__len__() - 1)):
			# 	list_737.append("AC" + results_737[a][0])
			return results_737

	def find_all_plane(self):				## check if the plane exist, return true or false
		cursor, db = self.connect()
		result = self.find_all_plane_helper(cursor)
		db.close()
		return result

	def find_all_plane_new_helper(self, cursor):
		if self.fleetName == "787-8": 
			sql_1 = "SELECT distinct AC FROM 787_FLIGHT "
			cursor.execute(sql_1)
			results_787 = cursor.fetchall() 
			list_787 = []
			for a in range((results_787.__len__())):
				plane_AC = results_787[a][0]
				list_787.append([])

				sql_1_1 = "select * from WARNING_CONDITION where AC= " + "\"" + plane_AC + "\""
				cursor.execute(sql_1_1)
				warning = cursor.fetchall()[0][1]
				list_787[a].append(plane_AC)
				list_787[a].append(warning)
			return list_787
		if self.fleetName == "757-200": 
			sql_2 = "SELECT distinct AC FROM 757_FLIGHT"
			cursor.execute(sql_2)
			results_757 = cursor.fetchall()
			list_757 = []
			for a in range((results_757.__len__())):
				plane_AC = results_757[a][0]
				list_757.append([])

				sql_1_1 = "select * from WARNING_CONDITION where AC= " + "\"" + plane_AC + "\""
				cursor.execute(sql_1_1)
				warning = cursor.fetchall()[0][1]
				list_757[a].append(plane_AC)
				list_757[a].append(warning)
			return list_757

		if self.fleetName == "737-800":
			sql_3 = "SELECT distinct AC FROM 737_FLIGHT"
			cursor.execute(sql_3)
			results_737 = cursor.fetchall()
			list_737 = []
			for a in range((results_737.__len__())):
				plane_AC = results_737[a][0]
				list_737.append([])

				sql_1_1 = "select * from WARNING_CONDITION where AC= " + "\"" + plane_AC + "\""
				cursor.execute(sql_1_1)
				warning = cursor.fetchall()[0][1]
				list_737[a].append(plane_AC)
				list_737[a].append(warning)
			return list_737

	def find_all_plane_new(self):
		cursor, db = self.connect()
		result = self.find_all_plane_new_helper(cursor)
		db.close()
		return result

	def find_basic_data_helper(self, cursor, table):
		if table == "737_FLIGHT":
			plane_type = "737-800"
		elif table == "757_FLIGHT":
			plane_type = "757-200"
		else:
			plane_type = "787-8"
		sql  = "SELECT * FROM " +  table + " where AC= \"" + self.id + "\" "
		cursor.execute(sql)
		result = cursor.fetchall()
		need = result[(result.__len__() - 1)]			## the last row
		need_2 = result[0]								## first row
		# a = need_2[3]
		# print(str(need_2[3]))					
		sql_2 = "select count(FLIGHT_TYPE) from " + table + " where AC = " + self.id + " and FLIGHT_TYPE=\"A检\""
		sql_3 = "select count(FLIGHT_TYPE) from " + table + " where AC = " + self.id + " and FLIGHT_TYPE=\"C检\""
		sql_4 = "select DATE_OF_PRODUCTION from PLANE where AC = " + self.id ##plane age
		sql_5 = "select count(*) from LMR_2018 where AC = "+ self.id 	##总故障次数
		sql_6 = "select count(distinct date_flight) from " + table + " where AC = " + self.id 	##total running time
		cursor.execute(sql_2)
		result2 = cursor.fetchall()
		cursor.execute(sql_3)
		result3 = cursor.fetchall()
		cursor.execute(sql_4)
		result4 = cursor.fetchall()
		year = 2018 - int((str(result4[0][0]))[0:4])
		total_month = year * 12 + 12 - int(str(result4[0][0])[5:7])			## age of the plane
		cursor.execute(sql_5)
		result5 = cursor.fetchall()
		failer_rate = round(result5[0][0] / need[28], 2)
		# failer_rate_helper = str(result5[0][0] / need[28])[2:6]
		# failer_rate = failer_rate_helper[:2] + "." + failer_rate_helper[2:] + "%"
		cursor.execute(sql_6)
		result6 = cursor.fetchall()
		availabe_days = result6[0][0]
		total_running_time = need[24]
		daily_use_rate = round(float((need[24] - need_2[24]) / result6[0][0]), 2)
		list1 = [float(need[22]), need[28], result2[0][0], result3[0][0], total_month, failer_rate, daily_use_rate, plane_type]	## need22: total flight time, need28: total rf, result2: A, result3: C
		return list1

	def find_basic_data(self):			## return the basic data of the plane
		cursor, db = self.connect()
		table = self.check_plane_type(cursor)
		result = self.find_basic_data_helper(cursor, table)
		db.close()
		return result
		## result[0]: total_flight_time, [1]: total rf 总起落, [2]: A检次数, [3]: C检次数, [4]: 机龄（单位：月）, [5]: 故障率（两位小数）, [6]: 使用率（h/天）, [7] 机型

	# def find_detail_data_helper(self, cursor, table):
	# 	sql  = "SELECT * FROM " +  table + " where AC= \"" + self.id + "\" "
	# 	sql_2 = "select * from LMR_2018 where AC = \"" + self.id + "\" "
	# 	cursor.execute(sql)
	# 	result = cursor.fetchall()			## fly record
	# 	cursor.execute(sql)
	# 	result2	= cursor.fetchall()			## 故障记录
	# 	sql_3 = "select * from REPLACE_REPORT where AC = \"" + self.id + "\" "
	# 	cursor.execute(sql)
	# 	result3	= cursor.fetchall()			## 维修记录
	# 	return result, result2, result3

	# def find_detail_data(self):
	# 	cursor, db = self.connect()
	# 	table = self.check_plane_type(cursor)
	# 	fly_record, error_record, maintenance_record = self.find_detail_data_helper(cursor, table)
	# 	db.close()
	# 	return fly_record, error_record, maintenance_record


	def find_fly_record_helper(self, cursor, table, page):
		flag = True
		# sql  = "SELECT * FROM " +  table + " where AC= \"" + self.id + "\" "

		sql_2 = "select count(*) from " + table + " where AC = " + str(self.id)
		cursor.execute(sql_2)
		lines = cursor.fetchall()
		number_of_pages = (lines[0][0] // self.per_page) + 1 
		if page > number_of_pages:
			page = number_of_pages
			flag = False
		page -= 1

		sql_3 = "describe " + table
		cursor.execute(sql_3)
		name = cursor.fetchall()
		name_list = []
		for i in range(name.__len__()):
			name_list.append(name[i][0])

		start = page * self.per_page
		sql = "SELECT * FROM " + table +  " where AC = " + str(self.id) + " limit " + str(start) + ", " + str(self.per_page) 
		cursor.execute(sql)
		fly_record = cursor.fetchall()
		if flag == True:
			number_of_pages = None
		return fly_record, number_of_pages, name_list


	def find_fly_record(self, page):
		cursor, db = self.connect()
		table = self.check_plane_type(cursor)
		fly_record, number_of_pages, name_list = self.find_fly_record_helper(cursor, table, page)
		db.close()
		return fly_record, number_of_pages, name_list

	def find_error_record_helper(self, cursor, page):
		flag = True
		sql_2 = "select count(*) from LMR_2018 where AC = " + str(self.id)
		cursor.execute(sql_2)
		lines = cursor.fetchall()
		number_of_pages = (lines[0][0] // self.per_page) + 1 
		if page > number_of_pages:
			page = number_of_pages
			flag = False
		page -= 1

		sql_3 = "describe LMR_2018"
		cursor.execute(sql_3)
		name = cursor.fetchall()
		name_list = []
		for i in range(name.__len__()):
			name_list.append(name[i][0])

		start = page * self.per_page
		sql = "select * from LMR_2018 where AC = \"" + self.id + "\" " + " limit " + str(start) + ", " + str(self.per_page)
		cursor.execute(sql)
		error_record = cursor.fetchall()
		if flag == True:
			number_of_pages = None
		return error_record, number_of_pages, name_list

	def find_error_record(self, page):
		cursor, db = self.connect()
		error_record, number_of_pages, name_list = self.find_error_record_helper(cursor, page)
		db.close()
		return error_record, number_of_pages, name_list

	def find_maintenance_record_helper(self, cursor, page):
		flag = True
		sql_2 = "select count(*) from REPLACE_REPORT where AC = " + str(self.id)
		cursor.execute(sql_2)
		lines = cursor.fetchall()
		number_of_pages = (lines[0][0] // self.per_page) + 1 
		if page > number_of_pages:
			page = number_of_pages
			flag = False
		page -= 1

		sql_3 = "describe REPLACE_REPORT"
		cursor.execute(sql_3)
		name = cursor.fetchall()
		name_list = []
		for i in range(name.__len__()):
			name_list.append(name[i][0])

		start = page * self.per_page
		sql = "select * from REPLACE_REPORT where AC = \"" + self.id + "\" " + " limit " + str(start) + ", " + str(self.per_page)
		cursor.execute(sql)
		maintenance_record = cursor.fetchall()
		if flag == True:
			number_of_pages = None
		return maintenance_record, number_of_pages, name_list

	def find_maintenance_record(self, page):
		cursor, db = self.connect()
		maintenance_record, number_of_pages, name_list = self.find_maintenance_record_helper(cursor, page)
		db.close()
		return maintenance_record, number_of_pages, name_list

	def convert_fleetName_to_table(self):
		if self.fleetName == "737-800":
			table = "737_FLIGHT"
		elif self.fleetName == "757-200":
			table = "757_FLIGHT"
		else:
			table = "787_FLIGHT"
		return table

	def calculate_total_helper(self, cursor):
		plane_tuple = self.find_all_plane_helper(cursor)
		table = self.convert_fleetName_to_table()
		total_flight_time = 0
		daily_use_rate = 0
		failer_rate = 0
		for i in range(plane_tuple.__len__()):
			sql = "SELECT * FROM " +  table + " where AC= \"" + str(plane_tuple[i][0]) + "\" "
			sql_2 = "select count(distinct date_flight) from " + table + " where AC = " + str(plane_tuple[i][0]) 	##total running time
			sql_3 = "select count(*) from LMR_2018 where AC = "+ str(plane_tuple[i][0]) 	##总故障次数
			cursor.execute(sql)
			result_1 = cursor.fetchall()
			cursor.execute(sql_2)
			result_2 = cursor.fetchall()
			cursor.execute(sql_3)
			result_3 = cursor.fetchall()
			need = result_1[(result_1.__len__() - 1)]		## last row
			need_2 = result_1[0]							## first row
			total_flight_time += float(need[22])
			daily_use_rate += round(float((need[24] - need_2[24]) / result_2[0][0]), 2)
			failer_rate += round(result_3[0][0] / need[28], 2)
		daily_use_rate /= plane_tuple.__len__()
		failer_rate /= plane_tuple.__len__()
		print(failer_rate)
		return 0

	def calculate_total(self):
		cursor, db = self.connect()
		result = self.calculate_total_helper(cursor)
		db.close()
		return result

	# def find_fleet_data_helper(self, cursor):
	# 	sql = "select * from FLEET_DATA where MODEL = \"" + self.fleetName + "\""
	# 	cursor.execute(sql)
	# 	result = cursor.fetchall()
	# 	list1 = []
	# 	for i in range(4):
	# 		list1.append(float(result[0][i+1]))
	# 	return list1

	# def find_fleet_data(self):
	# 	cursor, db = self.connect()
	# 	result = self.find_fleet_data_helper(cursor)
	# 	db.close()
	# 	return result
		##result[0]: total_flight_time, [1]: average_flight time, [2]: 使用率, [3]:故障率

	def find_fleet_data_helper(self, cursor):
		plane_tuple = self.find_all_plane_helper(cursor)
		table = self.convert_fleetName_to_table()
		# for i in range(plane_tuple.__len__()):
		sql_1 = "select max(total_flight_time) from " + table + " group by AC "
		cursor.execute(sql_1)
		total_flight_time_tuple = cursor.fetchall()
		total_flight_time = 0
		for i in range(total_flight_time_tuple.__len__()):
			total_flight_time += total_flight_time_tuple[i][0]
		sql_2 = "SELECT distinct AC FROM " + table
		cursor.execute(sql_2)
		total_plane = cursor.fetchall()
		number_of_plane = total_plane.__len__()
		average_flight_time = round((total_flight_time / number_of_plane), 2)
		sql_3 = "select (max(total_flight_time)-min(total_flight_time)) from " + table + " group by AC"
		sql_4 = "select count(distinct(date_flight)) from " + table + " group by AC"
		cursor.execute(sql_3)
		running_time = cursor.fetchall()
		cursor.execute(sql_4)
		availabe_days = cursor.fetchall()
		daily_use_rate = 0
		for i in range(running_time.__len__()):
			daily_use_rate += running_time[i][0] / availabe_days[i][0]
		daily_use_rate /= running_time.__len__()
		daily_use_rate = round(daily_use_rate, 2)
		sql_5 = "select max(sum_total_rf) from " + table + " group by AC"
		sql_6 = "select count(*) from LMR_2018 group by AC"

		
		# sql_6 = "select count(*) from LMR_2018 where AC = "
		cursor.execute(sql_5)
		total_cycle = cursor.fetchall()
		cursor.execute(sql_6)
		failer_time = cursor.fetchall()
		failer_rate = 0
		for i in range(number_of_plane):
			failer_rate += failer_time[i][0] / total_cycle[i][0]
		failer_rate /= number_of_plane
		failer_rate = round(failer_rate, 4)

		list1 = [total_flight_time, average_flight_time, daily_use_rate, failer_rate]
		return list1


	def find_fleet_data(self):
		cursor, db = self.connect()
		result = self.find_fleet_data_helper(cursor)
		db.close()
		return result
		##result[0]: total_flight_time, [1]: average_flight time, [2]: 使用率, [3]:故障率


	def model_function_helper(self, cursor):
		sql = "select * from 737_engine where AC = " + str(self.id)
		cursor.execute(sql)
		result = cursor.fetchall()
		
		list1 = []
		for i in range(result.__len__()):
			list1.append([])
		# first_line = ["MODEL", "ITEMNO", "PN", "SN", "AC", "POSITION", "DATE_U", "TSN_H", "TSO_H", "TST_H", "TSN_C", "TSO_C", "TST_C"]
		for i in range(result.__len__()):			
			for j in range(result[i].__len__()):
				list1[i].append(result[i][j])
		# list1.insert(0, first_line)

		data = pd.DataFrame(list1)
		data.columns = ["MODEL", "ITEMNO", "PN", "SN", "AC", "POSITION", "DATE_U", "TSN_H", "TSO_H", "TST_H", "TSN_C", "TSO_C", "TST_C"]
		return data

	def model_function(self, cursor):
		plane_type = self.check_plane_type(cursor)
		if plane_type == "737_FLIGHT":
			result = self.model_function_helper(cursor)
			model  = joblib.load('saved_model/my_model_1.m')
			result['age'] = (pd.to_datetime(datetime.date.today()) - pd.to_datetime(result['DATE_U'])).map(lambda x:x.days)
			result = result.drop(columns = ['MODEL','SN','AC','POSITION','DATE_U','ITEMNO', 'PN'])
			prediction = model.predict(result)
			return prediction[0], prediction[1]
		else:
			return "condition1", "condition1"

	def change_number_to_date(self, month):
		month_day = {"01": "30", "02": "28", "03": "31", "04": "30", "05": "31", "06": "30", "07": "31", "08": "31", "09": "30", "10": "31", "11": "30", "12": "31"}
		if month < 10:
			month = "0" + str(month)
		else:
			month = str(month)
		day = month_day[month]
		date_begin = "2018-" + month + "-01"
		date_end = "2018-" + month + "-" + day
		return date_begin, date_end

	def calculate_warning_helper(self, cursor):
		plane_tuple = self.find_all_plane_helper(cursor)
		table = self.convert_fleetName_to_table() 
		list1 = []
		list2 = []
		list3 = []
		# engine1, engine2 = self.model_function(cursor)
		# table = self.check_plane_type(cursor)
		for j in range(plane_tuple.__len__()):
			self.id = plane_tuple[j][0]
			list_performance = []
			for i in range(10):
				if i == 0:
					continue
				else:
					date_begin, date_end = self.change_number_to_date(i)
					sql = "select count(t.ATA)*1000/(max(s.sum_total_rf) - min(s.sum_total_rf))  from " + table + " as s, LMR_2018 as t where s.AC = " + "\"" + str(self.id) + "\"" +  " and s.date_flight between " + "\"" + date_begin + "\"" + " and " + "\"" + date_end + "\"" + " and t.AC = " + "\"" + str(self.id) + "\"" + " and t.date_rpt between " + "\"" + date_begin + "\"" + " and " + "\"" + date_end + "\""
					cursor.execute(sql)
					performance = cursor.fetchall()[0][0]
					if performance == None:
						performance = 0
					list_performance.append(performance)
			total_performance = 0
			for i in range(9):
				total_performance += list_performance[i]
			average_performance = total_performance / 9
			square = 0
			for i in range(9):
				square += list_performance[i] ** 2
			temp = (square - ((total_performance ** 2) / 9)) / 8
			sigema = math.sqrt(temp)
			warning_value = float(average_performance) + 2 * sigema
			list1.append(self.id)
			list2.append(warning_value)
			date_begin, date_end = self.change_number_to_date(10)
			sql_10 = "select count(t.ATA)*1000/(max(s.sum_total_rf) - min(s.sum_total_rf))  from " + table + " as s, LMR_2018 as t where s.AC = " + "\"" + str(self.id) + "\"" +  " and s.date_flight between " + "\"" + date_begin + "\"" + " and " + "\"" + date_end + "\"" + " and t.AC = " + "\"" + str(self.id) + "\"" + " and t.date_rpt between " + "\"" + date_begin + "\"" + " and " + "\"" + date_end + "\""
			cursor.execute(sql_10)
			performance_10 = cursor.fetchall()[0][0]
			if performance_10 == None:
				performance_10 = 0
			if performance_10 < warning_value:
				list3.append(True)
			else:
				list3.append(False)
		return list1, list3
			



	def calculate_warning(self):
		cursor, db = self.connect()
		result1, result2 = self.calculate_warning_helper(cursor)
		db.close()
		for i in range(result1.__len__()):
			print(result1[i])
		for i in range(result2.__len__()):
			print(result2[i])
		return result1, result2

	def check_warning_helper(self, cursor):
		engine1, engine2 = self.model_function(cursor)
		sql_1 = "select * from WARNING_CONDITION where AC= " + "\"" + str(self.id) + "\""
		cursor.execute(sql_1)
		warning = cursor.fetchall()[0][1]
		list1 = [engine1, engine2, warning]
		return list1
		

		

	def check_warning(self):
		cursor, db = self.connect()
		engine1, engine2, warning = self.check_warning_helper(cursor)
		db.close()
		return engine1, engine2, warning

	def dash_board_one_helper(self, cursor):
		plane_number = []
		for i in range(5):
			sql_1 = "select count(distinct AC) from 737_FLIGHT group by AC having max(total_flight_time) between " + str(i*10000) + " and " + str((i+1)*10000)
			sql_2 = "select count(distinct AC) from 757_FLIGHT group by AC having max(total_flight_time) between " + str(i*10000) + " and " + str((i+1)*10000)
			sql_3 = "select count(distinct AC) from 787_FLIGHT group by AC having max(total_flight_time) between " + str(i*10000) + " and " + str((i+1)*10000)
			cursor.execute(sql_1)
			temp1 = (cursor.fetchall()).__len__()
			cursor.execute(sql_2)
			temp2 = (cursor.fetchall()).__len__()
			cursor.execute(sql_3)
			temp3 = (cursor.fetchall()).__len__()
			total = temp1 + temp2 + temp3
			plane_number.append(total)
		return plane_number

	def dash_board_one(self):
		cursor, db = self.connect()
		result = self.dash_board_one_helper(cursor)
		db.close()
		return result

	def dash_board_two_helper(self, cursor):
		plane_cycle = []
		for i in range(10):
			sql_1 = "select count(distinct AC) from 737_FLIGHT group by AC having max(sum_total_rf) between " + str(i*3000) + " and " + str((i+1)*3000)
			sql_2 = "select count(distinct AC) from 757_FLIGHT group by AC having max(sum_total_rf) between " + str(i*3000) + " and " + str((i+1)*3000)
			sql_3 = "select count(distinct AC) from 787_FLIGHT group by AC having max(sum_total_rf) between " + str(i*3000) + " and " + str((i+1)*3000)
			cursor.execute(sql_1)
			temp1 = (cursor.fetchall()).__len__()
			cursor.execute(sql_2)
			temp2 = (cursor.fetchall()).__len__()
			cursor.execute(sql_3)
			temp3 = (cursor.fetchall()).__len__()
			total = temp1 + temp2 + temp3
			plane_cycle.append(total)
		return plane_cycle

	def dash_board_two(self):
		cursor, db = self.connect()
		result = self.dash_board_two_helper(cursor)
		db.close()
		return result

	def dash_board_three_helper(self, cursor):
		sql_1 = "select distinct AC , max(total_flight_time) from 737_FLIGHT group by AC order by max(total_flight_time) desc limit 0, 5"
		cursor.execute(sql_1)
		flight_time_tuple = cursor.fetchall()
		flight_time_ranking = []
		sql_2 = "select AC, (max(total_flight_time)-min(total_flight_time)) from 737_FLIGHT group by AC"
		sql_3 = "select AC, count(distinct(date_flight)) from 737_FLIGHT group by AC"
		cursor.execute(sql_2)
		temp2 = cursor.fetchall()

		cursor.execute(sql_3)
		temp3 = cursor.fetchall()

		daily_use_rate_helper = []
		for i in range(temp2.__len__()):
			temp_list = [round((temp2[i][1]/temp3[i][1]), 2), temp2[i][0]]
			daily_use_rate_helper.append(temp_list)
		daily_use_rate_helper.sort(reverse = True)
		daily_use_rate = []
		for i in range(5):
			daily_use_rate.append(daily_use_rate_helper[i])

		sql_4 = "select AC, max(sum_total_rf) from 737_FLIGHT group by AC"
		sql_5 = "select AC, count(*) from LMR_2018 group by AC"
		cursor.execute(sql_4)
		temp4 = cursor.fetchall()
		cursor.execute(sql_5)
		temp5 = cursor.fetchall()
		self.fleetName = "737-800"
		name_737 = self.find_all_plane()
		name_list = []
		list5 = []
		failer_rate_helper = []
		for i in range(name_737.__len__()):
			name_list.append(name_737[i][0])
		for i  in range(temp5.__len__()):
			if temp5[i][0] in name_list:
				list5.append([temp5[i][0], temp5[i][1]])
		for i in range(temp4.__len__()):
			temp_list = [round((list5[i][1]/temp4[i][1]), 4), list5[i][0]]
			failer_rate_helper.append(temp_list)
		failer_rate_helper.sort()
		failer_rate = []
		for i in range(5):								##弄成百分数
			failer_rate_helper[i][0] = round((failer_rate_helper[i][0] * 100), 2)
			failer_rate.append(failer_rate_helper[i])
		for i in range(5):
			flight_time_ranking.append([i+1, flight_time_tuple[i][0], flight_time_tuple[i][1]])
		for i in range(5):						##加序号
			# flight_time_tuple[i].insert(0,i)
			daily_use_rate[i].insert(0,i+1)
			failer_rate[i].insert(0,i+1)
		return flight_time_ranking, daily_use_rate, failer_rate

	def dash_board_three(self):
		cursor, db = self.connect()
		result1, result2, result3 = self.dash_board_three_helper(cursor)
		db.close()
		return result1, result2, result3
		## restult1 is flight_time_ranking, result2 is daily use_rate_ranking, result3 is the failer_rate_ranking

	def dash_board_four_helper(self, cursor):
		sql = "select * from WARNING_CONDITION"
		cursor.execute(sql)
		warning_tuple = cursor.fetchall()
		warning_list = []
		warning_list_update = []
		for i in range(warning_tuple.__len__()):
			if warning_tuple[i][1] == "FALSE":
				warning_list.append(warning_tuple[i][0])
			else:
				continue
		group = warning_list.__len__() // 4 + 1
		remain = warning_list.__len__() % 4
		for i in range(group):
			if i != (group - 1):
				warning_list_update.append([warning_list[i * 4 + 0], warning_list[i * 4 + 1], warning_list[i * 4 + 2], warning_list[i * 4 + 3]] )
			else:
				warning_list_update.append([])
				for j in range(remain):
					warning_list_update[group-1].append(warning_list[i * 4 + j])



		return warning_list_update

	def dash_board_four(self):
		cursor, db = self.connect()
		result = self.dash_board_four_helper(cursor)
		db.close()
		return result


	def engine_info_helper(self, cursor):
		table = self.check_plane_type(cursor)
		table = table[0:3] + "_engine"
		sql_1 = "select * from " + table + " where AC = " + "\"" + str(self.id) + "\""  + " and POSITION = 'L'"
		sql_2 = "select * from " + table + " where AC = " + "\"" + str(self.id) + "\""  + " and POSITION = 'R'"
		cursor.execute(sql_1)
		left = cursor.fetchall()
		cursor.execute(sql_2)
		right = cursor.fetchall()
		return left, right


	def engine_info(self):
		cursor, db = self.connect()
		left, right = self.engine_info_helper(cursor)
		db.close()
		return left, right







# test1 = search(id = "111300")		
# result = test1.check_exist()
# result3 = test1.find_basic_data() 
# result4 = test1.find_detail_data()
# print(result3)
# t0 = time.time()

# test2 = search(id = 115511)
# page = 7
# result5, a = test2.model_function()
# print(result5)

	
if __name__ == '__main__':
	# test3 = search(fleetName = "737-800")
	# result = test3.find_fleet_data()
	# result2  = test3.find_all_plane()
	# print(result2)
	# test4 = search()
	# a, b = test4.change_number_to_date(2)
	# print(a)
	# print(b)

	# test5 = search(fleetName = "787-8")
	# test5.calculate_warning()
	# test6 = search(id = "111300")
	# a, b, c = test6.check_warning()
	# print(a,b,c)
	# test7 = search(fleetName = "757-200")
	# test7.find_all_plane_new()
	# test8 = search()
	# a,b,c=test8.dash_board_three()
	# print(a, b, c)
	# result = test8.dash_board_four()
	# print(result)
	test9 = search(id = "111300")
	test9.engine_info()



