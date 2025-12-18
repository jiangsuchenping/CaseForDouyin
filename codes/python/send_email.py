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
import os


def send_text_email():
    """发送纯文本邮件"""
    # 邮件服务器配置 - 使用占位符，用户需要替换为实际配置
    SMTP_SERVER = 'smtp.example.com'  # SMTP服务器地址
    SMTP_PORT = 587  # SMTP服务器端口
    SMTP_USER = 'your_email@example.com'  # 发件人邮箱
    SMTP_PASSWORD = 'your_password'  # 发件人密码或授权码
    
    # 邮件内容
    sender = 'your_email@example.com'  # 发件人邮箱
    receiver = 'recipient@example.com'  # 收件人邮箱
    subject = 'Python 纯文本邮件测试'
    body = '这是一封使用 Python 发送的纯文本邮件。'
    
    try:
        # 创建纯文本邮件对象
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['From'] = formataddr(['发件人名称', sender])
        msg['To'] = formataddr(['收件人名称', receiver])
        msg['Subject'] = Header(subject, 'utf-8')
        
        print('纯文本邮件内容已准备好：')
        print(f'  发件人：{sender}')
        print(f'  收件人：{receiver}')
        print(f'  主题：{subject}')
        print(f'  正文：{body}')
        print('  （注：未实际发送，仅展示示例）')
        
        # 连接服务器并发送（默认注释掉，防止误发）
        # server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        # server.starttls()
        # server.login(SMTP_USER, SMTP_PASSWORD)
        # server.sendmail(sender, [receiver], msg.as_string())
        # server.quit()
        # print('纯文本邮件发送成功！')
        
        return True
    except Exception as e:
        print(f'纯文本邮件示例生成失败：{str(e)}')
        return False


def send_html_email():
    """发送HTML格式邮件"""
    # 邮件服务器配置 - 使用占位符，用户需要替换为实际配置
    SMTP_SERVER = 'smtp.example.com'  # SMTP服务器地址
    SMTP_PORT = 587  # SMTP服务器端口
    SMTP_USER = 'your_email@example.com'  # 发件人邮箱
    SMTP_PASSWORD = 'your_password'  # 发件人密码或授权码
    
    # 邮件内容
    sender = 'your_email@example.com'  # 发件人邮箱
    receiver = 'recipient@example.com'  # 收件人邮箱
    subject = 'Python HTML邮件测试'
    
    # HTML邮件正文
    html_body = '''
    <html>
    <body>
        <h1>Python HTML邮件测试</h1>
        <p>这是一封使用 Python 发送的 HTML 格式邮件。</p>
        <p>可以包含 <a href="https://www.python.org">链接</a> 和 <strong>格式化文本</strong>。</p>
    </body>
    </html>
    '''
    
    try:
        # 创建HTML邮件对象
        msg = MIMEText(html_body, 'html', 'utf-8')
        msg['From'] = formataddr(['发件人名称', sender])
        msg['To'] = formataddr(['收件人名称', receiver])
        msg['Subject'] = Header(subject, 'utf-8')
        
        print('HTML邮件内容已准备好：')
        print(f'  发件人：{sender}')
        print(f'  收件人：{receiver}')
        print(f'  主题：{subject}')
        print(f'  HTML正文长度：{len(html_body)} 字符')
        print('  （注：未实际发送，仅展示示例）')
        
        # 连接服务器并发送（默认注释掉，防止误发）
        # server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        # server.starttls()
        # server.login(SMTP_USER, SMTP_PASSWORD)
        # server.sendmail(sender, [receiver], msg.as_string())
        # server.quit()
        # print('HTML邮件发送成功！')
        
        return True
    except Exception as e:
        print(f'HTML邮件示例生成失败：{str(e)}')
        return False


def send_email_with_attachment():
    """发送带附件的邮件"""
    # 邮件服务器配置 - 使用占位符，用户需要替换为实际配置
    SMTP_SERVER = 'smtp.example.com'  # SMTP服务器地址
    SMTP_PORT = 587  # SMTP服务器端口
    SMTP_USER = 'your_email@example.com'  # 发件人邮箱
    SMTP_PASSWORD = 'your_password'  # 发件人密码或授权码
    
    # 邮件内容
    sender = 'your_email@example.com'  # 发件人邮箱
    receiver = 'recipient@example.com'  # 收件人邮箱
    subject = 'Python 带附件邮件测试'
    body = '这是一封带附件的邮件，附件为测试文件。'
    
    try:
        # 创建带附件的邮件对象
        msg = MIMEMultipart()
        msg['From'] = formataddr(['发件人名称', sender])
        msg['To'] = formataddr(['收件人名称', receiver])
        msg['Subject'] = Header(subject, 'utf-8')
        
        # 添加正文
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # 添加附件（使用当前目录下的hundred_chickens.py作为示例附件）
        attachment_file = 'hundred_chickens.py'
        if os.path.exists(attachment_file):
            with open(attachment_file, 'rb') as f:
                part = MIMEApplication(f.read())
                part.add_header('Content-Disposition', f'attachment; filename="{attachment_file}"')
                msg.attach(part)
            print(f'已添加附件：{attachment_file}')
        else:
            print(f'示例附件文件不存在：{attachment_file}')
        
        print('带附件的邮件内容已准备好：')
        print(f'  发件人：{sender}')
        print(f'  收件人：{receiver}')
        print(f'  主题：{subject}')
        print(f'  正文：{body}')
        print('  （注：未实际发送，仅展示示例）')
        
        # 连接服务器并发送（默认注释掉，防止误发）
        # server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        # server.starttls()
        # server.login(SMTP_USER, SMTP_PASSWORD)
        # server.sendmail(sender, [receiver], msg.as_string())
        # server.quit()
        # print('带附件的邮件发送成功！')
        
        return True
    except Exception as e:
        print(f'带附件的邮件示例生成失败：{str(e)}')
        return False


if __name__ == '__main__':
    print('Python 发送邮件示例')
    print('==================')
    print('\n注意：此示例不包含真实的SMTP服务器配置，请用户替换为自己的配置后再实际发送。')
    
    # 交互式演示，直接展示所有功能
    print('\n1. 演示发送纯文本邮件（仅展示代码逻辑，不实际发送）：')
    send_text_email()
    
    print('\n2. 演示发送HTML格式邮件（仅展示代码逻辑，不实际发送）：')
    send_html_email()
    
    print('\n3. 演示发送带附件的邮件（仅展示代码逻辑，不实际发送）：')
    send_email_with_attachment()
    
    print('\n所有演示完成！')
    print('\n实际使用时，请：')
    print('1. 替换SMTP服务器配置（服务器地址、端口、用户名、密码）')
    print('2. 替换发件人和收件人邮箱地址')
    print('3. 根据需要修改邮件内容')
    print('4. 取消相关注释以实际发送邮件')