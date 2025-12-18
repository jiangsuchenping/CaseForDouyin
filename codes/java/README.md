# Java 邮件发送示例

## 项目简介

这是一个使用Java语言编写的邮件发送示例程序，演示如何使用JavaMail API发送各种类型的邮件。

## 功能特性

- ✅ 发送纯文本邮件
- ✅ 发送HTML格式邮件  
- ✅ 发送带附件的邮件
- ✅ 安全的占位符配置
- ✅ 详细的代码注释和文档

## 环境要求

- Java 8 或更高版本
- JavaMail API (javax.mail)
- Java Activation Framework (javax.activation)

## 依赖安装

### 方式1：使用Maven（推荐）

创建 `pom.xml` 文件：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.example</groupId>
    <artifactId>email-sender</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>
    
    <properties>
        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
    
    <dependencies>
        <!-- JavaMail API -->
        <dependency>
            <groupId>com.sun.mail</groupId>
            <artifactId>javax.mail</artifactId>
            <version>1.6.2</version>
        </dependency>
        
        <!-- Java Activation Framework -->
        <dependency>
            <groupId>javax.activation</groupId>
            <artifactId>activation</artifactId>
            <version>1.1.1</version>
        </dependency>
    </dependencies>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>8</source>
                    <target>8</target>
                </configuration>
            </plugin>
            
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.2.4</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                        <configuration>
                            <transformers>
                                <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                    <mainClass>SendEmail</mainClass>
                                </transformer>
                            </transformers>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### 方式2：手动下载JAR包

1. 下载以下JAR文件：
   - [javax.mail-1.6.2.jar](https://repo1.maven.org/maven2/com/sun/mail/javax.mail/1.6.2/)
   - [activation-1.1.1.jar](https://repo1.maven.org/maven2/javax/activation/activation/1.1.1/)

2. 将JAR文件放在同一目录下

## 使用方法

### 1. 配置邮件服务器

编辑 `SendEmail.java` 文件，修改以下配置：

```java
// SMTP服务器配置
private static final String SMTP_HOST = "your.smtp.server.com";
private static final String SMTP_PORT = "587";
private static final String USERNAME = "your_email@example.com";
private static final String PASSWORD = "your_password";

// 邮件内容配置
private static final String SENDER_EMAIL = "your_email@example.com";
private static final String SENDER_NAME = "Your Name";
private static final String RECIPIENT_EMAIL = "recipient@example.com";
private static final String RECIPIENT_NAME = "Recipient Name";
```

### 2. 编译和运行

#### 使用Maven：
```bash
# 编译
mvn clean compile

# 运行
mvn exec:java -Dexec.mainClass="SendEmail"

# 或者打包后运行
mvn clean package
java -jar target/email-sender-1.0.0.jar
```

#### 手动编译：
```bash
# 编译
javac -cp ".:javax.mail-1.6.2.jar:activation-1.1.1.jar" SendEmail.java

# 运行
java -cp ".:javax.mail-1.6.2.jar:activation-1.1.1.jar" SendEmail
```

#### Windows系统：
```cmd
# 编译
javac -cp ".;javax.mail-1.6.2.jar;activation-1.1.1.jar" SendEmail.java

# 运行
java -cp ".;javax.mail-1.6.2.jar;activation-1.1.1.jar" SendEmail
```

## 功能演示

程序运行后会演示三种邮件发送功能：

1. **纯文本邮件** - 发送简单的文本内容
2. **HTML格式邮件** - 发送包含HTML格式的邮件
3. **带附件邮件** - 发送包含文件附件的邮件

## 安全提示

⚠️ **重要安全建议：**

1. **使用占位符配置** - 代码默认使用示例配置，不会暴露真实密码
2. **实际使用时请替换配置** - 将占位符替换为您的实际邮件服务器配置
3. **使用应用专用密码** - 建议使用应用专用密码而非主密码
4. **保护配置文件** - 不要将包含真实密码的代码提交到版本控制
5. **启用两步验证** - 为您的邮箱账户启用两步验证

## 常见问题

### Q: 出现 `javax.mail.AuthenticationFailedException`
**A:** 检查用户名和密码是否正确，确保使用的是应用专用密码（如果邮箱提供商支持）。

### Q: 出现 `javax.mail.MessagingException: Could not connect to SMTP host`
**A:** 检查SMTP服务器地址和端口是否正确，确保网络连接正常。

### Q: 附件文件找不到
**A:** 确保附件文件存在于程序运行的当前目录中。

### Q: 中文乱码问题
**A:** 代码已设置UTF-8编码，确保您的开发环境也使用UTF-8编码。

## 扩展功能

您可以基于此示例扩展以下功能：
- ✅ 批量邮件发送
- ✅ 邮件模板系统
- ✅ 邮件队列处理
- ✅ 邮件发送日志记录
- ✅ 邮件发送状态监控

## 技术支持

如遇到问题，请检查：
1. Java版本是否符合要求
2. 依赖库是否正确安装
3. 网络连接是否正常
4. 邮件服务器配置是否正确

## 版本历史

- **v1.0.0** (2025-12-18) - 初始版本，支持三种邮件类型发送