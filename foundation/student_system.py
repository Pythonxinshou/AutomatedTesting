# -*- coding:utf-8 -*-
# @Time : 2021/11/14 20:48
# @Author : 朱树剑
# @File : student_system.py



student_list = []


def add_stu():
    student_dict = {}
    id = input('请输入学号：')
    for i in student_list:
        if id == i['id']:
            print('编号已存在')
            print(student_list)
            return
    name = input('请输入姓名：')
    age = input('请输入年龄：')
    student_dict['id'] = id
    student_dict['name'] = name
    student_dict['age'] = age
    student_list.append(student_dict)
    print(student_list)


def del_stu():
    id = input('请输入需要删除的学生编号：')
    for i in student_list:
        if id == i['id']:
            student_list.remove(i)
            print(student_list)
            return
    print('该学号不存在')
    print(student_list)

def rev_stu():
    id = input('请输入需要修改的学生编号：')
    for i in student_list:
        if id == i['id']:
            name = input('新的名字：')
            age = input('新的年龄：')
            i['name'] = name
            i['age']=age
            print(student_list)
            return
    print('该学号不存在')
    print(student_list)


def sel_stu():
    id = input('请输入需要查询的学生编号：')
    for i in student_list:
        if id == i['id']:
            print(i.items())
            return
    print('该学号不存在')


while 1:
    num = str(input('''
    -------------欢迎进入学生管理系统-------------
    可选择的系统功能:
    O:显示所有学员信息
    1:添加一个学员信息
    2:删除个学员信息
    3:修改个学员信息
    4:查询一个学员信息
    exit:退出学生管理系统
    请输入需要的系统功能号：'''))
    if num == '0':
        print(student_list)
    elif num == '1':
        add_stu()
    elif num == '2':
        del_stu()
    elif num == '3':
        rev_stu()
    elif num == '4':
        sel_stu()
    elif num == 'exit':
        break
    else:
        print('输入功能号有误，请重新输入。')