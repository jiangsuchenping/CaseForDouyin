#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 发送邮件示例代码

本脚本演示了如何使用 Python 的 smtplib 和 email 库发送邮件，包括：
1. 发送纯文本邮件
2. 发送 HTML 格式邮件
3. 发送带附件的邮件

使用说明：
1. 修改邮件服务器配置（SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD）
2. 修改发件人、收件人等信息
3. 运行脚本：python send_email.py
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from email.utils import formataddr
import os

def send_text_email():
    """发送纯文本邮件"""
    # 邮件服务器配置
    SMTP_SERVER = 'smtp.notice.e-medicine.cn'  # SMTP服务器地址
    SMTP_PORT = 25  # SMTP服务器端口（通常为25，SSL为465，TLS为587）
    SMTP_USER = 'notification@notice.e-medicine.cn'  # 发件人邮箱
    SMTP_PASSWORD = ''  # 发件人密码
    
    # 邮件内容
    sender = 'notification@notice.e-medicine.cn'  # 发件人邮箱
    receiver = ''  # 收件人邮箱
    subject = 'Python 纯文本邮件测试'
    body = '这是一封使用 Python smtplib 库发送的纯文本邮件。\n\n祝好！'
    
    try:
        # 创建邮件对象
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['From'] = formataddr(['发件人名称', sender])  # 发件人信息
        msg['To'] = formataddr(['收件人名称', receiver])  # 收件人信息
        msg['Subject'] = Header(subject, 'utf-8')  # 邮件主题
        
        # 连接邮件服务器并发送邮件
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        # 如果需要TLS加密
        # server.starttls()
        # 登录邮件服务器
        server.login(SMTP_USER, SMTP_PASSWORD)
        # 发送邮件
        server.sendmail(sender, [receiver], msg.as_string())
        # 关闭连接
        server.quit()
        
        print('纯文本邮件发送成功！')
        return True
    except Exception as e:
        print(f'纯文本邮件发送失败：{str(e)}')
        return False

def send_html_email():
    """发送HTML格式邮件"""
    # 邮件服务器配置
    SMTP_SERVER = 'smtp.notice.e-medicine.cn'  # SMTP服务器地址
    SMTP_PORT = 25  # SMTP服务器端口（通常为25，SSL为465，TLS为587）
    SMTP_USER = 'notification@notice.e-medicine.cn'  # 发件人邮箱
    SMTP_PASSWORD = ''  # 发件人密码
    
    # 邮件内容
    sender = 'notification@notice.e-medicine.cn'  # 发件人邮箱
    receiver = ''  # 收件人邮箱
    subject = 'Python HTML 邮件测试'
    
    # HTML内容
    html_body = '''
    <html>
        <body>
            <h1>Python HTML 邮件测试</h1>
            <p>这是一封使用 Python 发送的 HTML 格式邮件。</p>
            <p>可以包含：</p>
            <ul>
                <li>标题标签</li>
                <li>段落标签</li>
                <li>列表标签</li>
                <li>以及其他 HTML 元素</li>
            </ul>
            <p style="color: blue;">还可以使用 CSS 样式！</p>
        </body>
    </html>
    '''
    
    try:
        # 创建邮件对象
        msg = MIMEText(html_body, 'html', 'utf-8')
        msg['From'] = formataddr(['发件人名称', sender])
        msg['To'] = formataddr(['收件人名称', receiver])
        msg['Subject'] = Header(subject, 'utf-8')
        
        # 连接服务器并发送
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        # server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(sender, [receiver], msg.as_string())
        server.quit()
        
        print('HTML 邮件发送成功！')
        return True
    except Exception as e:
        print(f'HTML 邮件发送失败：{str(e)}')
        return False

def send_email_with_attachment():
    """发送带附件的邮件"""
    # 邮件服务器配置
    SMTP_SERVER = 'smtp.notice.e-medicine.cn'  # SMTP服务器地址
    SMTP_PORT = 25  # SMTP服务器端口（通常为25，SSL为465，TLS为587）
    SMTP_USER = 'notification@notice.e-medicine.cn'  # 发件人邮箱
    SMTP_PASSWORD = ''  # 发件人密码
    
    # 邮件内容
    sender = 'notification@notice.e-medicine.cn'  # 发件人邮箱
    receiver = ''  # 收件人邮箱
    subject = 'Python 带附件邮件测试'
    
    # 邮件正文
    body = '这是一封带附件的邮件，附件为当前目录下的 hundred_chickens.py 文件。'
    
    try:
        # 创建带附件的邮件对象
        msg = MIMEMultipart()
        msg['From'] = formataddr(['发件人名称', sender])
        msg['To'] = formataddr(['收件人名称', receiver])
        msg['Subject'] = Header(subject, 'utf-8')
        
        # 添加正文
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # 添加附件（假设当前目录下有 hundred_chickens.py 文件）
        attachment_file = 'hundred_chickens.py'
        if os.path.exists(attachment_file):
            with open(attachment_file, 'rb') as f:
                part = MIMEApplication(f.read())
                part.add_header('Content-Disposition', f'attachment; filename="{attachment_file}"')
                msg.attach(part)
            print(f'已添加附件：{attachment_file}')
        else:
            print(f'附件文件不存在：{attachment_file}')
        
        # 连接服务器并发送
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        # server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(sender, [receiver], msg.as_string())
        server.quit()
        
        print('带附件的邮件发送成功！')
        return True
    except Exception as e:
        print(f'带附件的邮件发送失败：{str(e)}')
        return False

if __name__ == '__main__':
    print('Python 发送邮件示例')
    print('==================')
    
    # 非交互式演示，直接展示所有功能
    print('\n1. 演示发送纯文本邮件（仅展示代码逻辑，不实际发送）：')
    send_text_email()
    
    print('\n2. 演示发送HTML格式邮件（仅展示代码逻辑，不实际发送）：')
    send_html_email()
    
    print('\n3. 演示发送带附件的邮件（仅展示代码逻辑，不实际发送）：')
    send_email_with_attachment()
    
    print('\n所有演示完成！')
