from selenium import webdriver
from selenium.webdriver.support.select import Select


users = [
	{
		'first_name': 'pedro',
		'last_name': 'willian',
		'email': 'pedro@gmail.com',
		'phone': '9635656445',
		'address': 'testestes',
		'city': 'asdssss',
		'state': 'Colorado',
		'zip': '12323',
		'website': 'https://www.google.com',
		'hosting': 'yes',
		'comment': 'Agora eu era um heroi'


	},
	{
		'first_name': 'jordan',
		'last_name': 'smith',
		'email': 'jordan@gmail.com',
		'phone': '9635656345',
		'address': 'testestes',
		'city': 'asdssss',
		'state': 'Florida',
		'zip': '12323',
		'website': 'https://www.facebook.com',
		'hosting': 'no',
		'comment': 'Era uma vez um anjo caido'

	},
]

link = 'https://www.seleniumeasy.com/test/input-form-demo.html'
class BotInsertValues:
	def __init__(self, request, users):
		self.driver = webdriver.Firefox()
		self.users = users
		self.request = request

	def clear_field(self):
		select_element = self.driver.find_element_by_name('state')
		select_object = Select(select_element)
		count = 0
		while count < len(self.users):
			list_field = list(self.users[count].keys())
			for count_field in list_field:
				field_clear = self.driver.find_element_by_name(count_field)
				if count_field == 'state':
					field_clear.click()
					select_object.select_by_index(0)
				elif count_field == 'hosting':
					continue
				else:
					field_clear.clear()
			count+=1

	def open(self):
		self.driver.get(self.request)

	def insert_values(self):
		select_element = self.driver.find_element_by_name('state')
		select_object = Select(select_element)
		count = 0
		while count < len(self.users):
			list_field = list(self.users[count].keys())
			for count_field in list_field:
				field_insert = self.driver.find_element_by_name(count_field)
				field_insert.send_keys(self.users[count][count_field])
				if count_field == 'state':
					select_object.select_by_visible_text(self.users[count][count_field])
				elif count_field == 'hosting' and self.users[count][count_field] == 'yes':
					self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/section/form/fieldset/div[10]/div/div[2]/label/input').click()
				elif count_field == 'hosting' and self.users[count][count_field] == 'no':
					self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/section/form/fieldset/div[10]/div/div[1]/label/input').click()
			count+=1
			self.driver.find_element_by_class_name('btn').click()
			self.clear_field()
		if count == len(self.users):
			self.driver.refresh()
	def main(self):
		self.open()
		self.insert_values()

bot_insert = BotInsertValues(link, users)
bot_insert.main()


