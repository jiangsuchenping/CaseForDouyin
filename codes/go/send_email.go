package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/smtp"
	"os"
)

// SMTPConfig 存储SMTP服务器配置信息
type SMTPConfig struct {
	Server   string `json:"server"`   // SMTP服务器地址
	Port     int    `json:"port"`     // SMTP服务器端口
	Username string `json:"username"` // SMTP账号
	Password string `json:"password"` // SMTP密码
}

// Email 存储邮件信息
type Email struct {
	From    string   `json:"from"`    // 发件人邮箱
	To      []string `json:"to"`      // 收件人邮箱列表
	Subject string   `json:"subject"` // 邮件主题
	Body    string   `json:"body"`    // 邮件正文
}

// loadConfig 从配置文件加载SMTP配置
// 参数:
//   filePath: 配置文件路径
// 返回值:
//   *SMTPConfig: 加载的配置信息
//   error: 加载过程中发生的错误
func loadConfig(filePath string) (*SMTPConfig, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return nil, fmt.Errorf("打开配置文件失败: %v", err)
	}
	defer file.Close()

	data, err := ioutil.ReadAll(file)
	if err != nil {
		return nil, fmt.Errorf("读取配置文件失败: %v", err)
	}

	var config SMTPConfig
	if err := json.Unmarshal(data, &config); err != nil {
		return nil, fmt.Errorf("解析配置文件失败: %v", err)
	}

	return &config, nil
}

// sendEmail 使用SMTP发送邮件
// 参数:
//   config: SMTP服务器配置
//   email: 邮件信息
// 返回值:
//   error: 发送过程中发生的错误
func sendEmail(config *SMTPConfig, email *Email) error {
	// 构建邮件内容
	message := fmt.Sprintf("From: %s\r\n", email.From)
	message += fmt.Sprintf("To: %s\r\n", email.To[0])
	message += fmt.Sprintf("Subject: %s\r\n\r\n", email.Subject)
	message += email.Body

	// 构建SMTP服务器地址
	smtpAddr := fmt.Sprintf("%s:%d", config.Server, config.Port)

	// 认证信息
	auth := smtp.PlainAuth("", config.Username, config.Password, config.Server)

	// 发送邮件
	if err := smtp.SendMail(smtpAddr, auth, email.From, email.To, []byte(message)); err != nil {
		return fmt.Errorf("发送邮件失败: %v", err)
	}

	return nil
}

func main() {
	// 加载配置文件
	config, err := loadConfig("smtp_config.json")
	if err != nil {
		fmt.Printf("配置加载失败: %v\n", err)
		return
	}

	// 创建邮件
	email := &Email{
		From:    config.Username,                // 使用配置的用户名作为发件人
		To:      []string{"recipient@example.com"}, // 收件人邮箱
		Subject: "Go语言发送邮件测试",            // 邮件主题
		Body:    "这是一封使用Go语言发送的测试邮件。",  // 邮件正文
	}

	// 发送邮件
	if err := sendEmail(config, email); err != nil {
		fmt.Printf("邮件发送失败: %v\n", err)
		return
	}

	fmt.Println("邮件发送成功!")
}
