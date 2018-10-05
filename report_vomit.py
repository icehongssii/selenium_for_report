from selenium import webdriver
from datetime import datetime as dt
driver = webdriver.Chrome(executable_path=r'/Users/icehongssi/hard_way_python/chromedriver')
import time
from config import info


driver.get(info['uploader_endpoints'])
driver.implicitly_wait(3)


#COMMON
########################################################
def move_to_contents(number):
    driver.find_elements_by_tag_name('li')[number].click()
    if(number==4):
        time.sleep(50)
        return None
    time.sleep(20)


def click_submit_btn(class_name, name):
    print(name+"has been clicked!")
    driver.find_elements_by_class_name(class_name)[0].click()
    time.sleep(20)

def click_latest_page():
    paginator=(driver.find_elements_by_class_name('mat-paginator-range-label')[0])
    print(paginator)

    total_contents_number = int(paginator.text.split("of")[1])/10

    for pagination in range(total_contents_number):
        next_btn = driver.find_elements_by_class_name("mat-paginator-navigation-next")[0]
        next_btn.click()

    return total_contents_number

def find_contents(keywords):
    contents_list = driver.find_elements_by_tag_name("tr")
    indexNumber = 0

    for idx, contents in enumerate(contents_list):
        if keywords in contents.text:
            indexNumber=idx

    found_contents_container = driver.find_elements_by_tag_name("tr")[indexNumber]

    return found_contents_container
########################################################

#INIT data
########################################################
def contents():
    date = str(dt.today().strftime("%Y-%m-%d"))
    hour = str(dt.now().strftime("%H"))

    contents_format="T00:00:00+00:00"
    apm="AM"

    if(int(hour)>12):
        flag="T12:00:00+00:00"
        apm="PM"

    created_at="{date}{flag}".format(**locals())
    title="{date}{apm} Report".format(**locals())

    return {'created_at':created_at,
            'title':title}
########################################################


#Add login
########################################################
def login(email, pw):
    id_form = driver.find_elements_by_class_name('form-field')[0]
    id_form.send_keys(email)

    pw_form = driver.find_elements_by_class_name('form-field')[1]
    pw_form.send_keys(pw)

    submit_btn = driver.find_elements_by_class_name('btn')[0]
    submit_btn.click()

    time.sleep(20)
########################################################

#Add msg
########################################################
def add_messages(name, _description):
    user_list_btn = driver.find_elements_by_class_name('mat-input-infix')[0]
    user_list_btn.click()

    users = driver.find_elements_by_class_name('mat-option-text')
    for user in users[:10]:
        if name.split(" ")[0] in user.text:
            user.click()
            break

    description = driver.find_elements_by_tag_name('textarea')[0]
    description.send_keys(_description)

    visible_btn = driver.find_elements_by_class_name('mat-checkbox-inner-container')[0]
    visible_btn.click()

    activate_btn = driver.find_elements_by_class_name('btn')[0]
    activate_btn.click()

    time.sleep(20)
########################################################


#Add con
########################################################
def add_conversation(name,msg_id):
    user_list_btn = driver.find_elements_by_class_name('mat-input-infix')[0]
    user_list_btn.click()

    add_conversation_write_type()
    add_conversation_write_name(name)
    add_conversation_write_msgId(msg_id)

    activate_btn=driver.find_elements_by_class_name('btn-primary')[0]
    driver.execute_script("arguments[0].click();", activate_btn)

    time.sleep(20)

def add_conversation_write_type():
    conversation_type_btn = driver.find_elements_by_class_name('mat-input-infix')[2]
    driver.execute_script("arguments[0].click();", conversation_type_btn)
    conversation_type = driver.find_elements_by_class_name('mat-option-text')
    for conversation in conversation_type:
        if "Public" in conversation.text:
            conversation.click()
            break

def add_conversation_write_name(name):
    users = driver.find_elements_by_class_name('mat-option-text')
    for user in users[:10]:
        if name.split(" ")[0] in user.text:
            user.click()
            break

def add_conversation_write_msgId(msg_id):
    msg_ids_btn = driver.find_elements_by_class_name('mat-input-infix')[3]
    driver.execute_script("arguments[0].click();", msg_ids_btn)
    time.sleep(5)
    msg_ids= driver.find_elements_by_class_name('mat-option-text')
    for id in msg_ids:
        if msg_id in id.text:
            driver.execute_script("arguments[0].click();", id)
            break
########################################################

#Edit msg
########################################################
def select_conversation_id():
    driver.find_elements_by_class_name("mat-input-infix")[2].click()
    conversation_ids = driver.find_elements_by_class_name('mat-option-text')
    for id in conversation_ids:
        if con_id in id.text:
            id.click()
            break
########################################################


#Add report
########################################################
def addReport(name, con_id, date_information):
    report = get_report()
    author = driver.find_elements_by_class_name('form-field')[0].send_keys(name) #Author
    title = driver.find_elements_by_class_name('form-field')[1].send_keys(date_information['title']) #title
    conversation_id = driver.find_elements_by_class_name('form-field')[2].send_keys(con_id)
    description = driver.find_elements_by_class_name('form-field')[3].send_keys(date_information['title']) #title
    created_at = driver.find_elements_by_class_name('form-field')[4].send_keys(date_information['created_at'])
    tag = driver.find_elements_by_class_name('form-field')[6].send_keys('ETH') #created_at
    content = driver.find_elements_by_tag_name("textarea")[1].send_keys(report())
    add=driver.find_elements_by_class_name('btn-primary')[2].click()

def get_date_for_report():
    date = str(dt.today().strftime("%Y-%d-%m"))
    hour = int(dt.now().strftime("%H"))

    time_format = "0100BST 2000EST 0800HKT.txt"
    if(hour>12):
        time_format = "1300BST 0800EST 2000HKT.txt"

    file_name = "{date} {time_format}".format(**locals())
    return file_name

def get_report():
    file_name = get_date_for_report()
    file = open("/Users/icehongssi/Downloads/{file_name}".format(**locals()), 'rb')
    data = file.read()
    file.close()

    return data.decode('utf-8', 'ignore')
########################################################





date_information = contents()
name = info['uploader_name']
email = info['uploader_email']
pw = info['uploader_pw']


#Login
##################################
login(email, pw)
##################################



#Add msg
##################################
move_to_contents(8)
click_submit_btn('btn', 'add')
add_messages(name, date_information['title'])
click_latest_page()
msg_id=find_contents(date_information['title']).find_elements_by_tag_name("td")[0].text
##################################

#Add con
##################################
move_to_contents(7)
click_submit_btn('btn', 'add')
add_conversation(name, msg_id)
###############################

#Activate con
###############################
click_latest_page()
result_tr=find_contents("false")
con_id=result_tr.find_elements_by_tag_name("td")[1].text
edit_btn=result_tr.find_elements_by_class_name("edit-icon")[0].click()
time.sleep(10)
click_submit_btn('btn-success', 'activate')
click_submit_btn('btn-primary', 'update')
###############################

#Edit msg
##################################
move_to_contents(8)
click_latest_page()
edit_btn = find_contents(msg_id).find_elements_by_tag_name("td")[4].click()
time.sleep(20)
select_conversation_id()
click_submit_btn('btn', 'submit')
###################################

#Add report
###################################
move_to_contents(4)
click_submit_btn('btn', 'add')
addReport(name, con_id, date_information)
time.sleep(50)
###################################

#update report
###################################
click_latest_page()
result_tr=find_contents(date_information['title'])
edit_btn=result_tr.find_elements_by_class_name("edit-icon")[0].click()
time.sleep(10)
click_submit_btn('btn-success', 'activate')
add=driver.find_elements_by_class_name('btn-primary')[2].click()
time.sleep(50)
############################

driver.close()
