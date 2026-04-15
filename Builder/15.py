from dataclasses import dataclass, field

@dataclass
class Email:
    from_addr: str = ""
    to: list = field(default_factory=list)
    subject: str = ""
    cc: list = field(default_factory=list)
    bcc: list = field(default_factory=list)
    text_body: str = ""
    html_body: str = ""
    attachments: list = field(default_factory=list)

    def __str__(self):
        return (
            f"От: {self.from_addr}\n"
            f"Кому: {', '.join(self.to)}\n"
            f"Тема: {self.subject}\n"
            f"Вложений: {len(self.attachments)}"
        )

class EmailBuilder:
    def __init__(self):
        self._email = Email()

    def set_from(self, from_addr: str):
        self._email.from_addr = from_addr
        return self

    def add_to(self, recipient: str):
        self._email.to.append(recipient)
        return self

    def add_cc(self, cc_recipient: str):
        self._email.cc.append(cc_recipient)
        return self

    def add_bcc(self, bcc_recipient: str):
        self._email.bcc.append(bcc_recipient)
        return self

    def set_subject(self, subject: str):
        self._email.subject = subject
        return self

    def set_text_body(self, text: str):
        self._email.text_body = text
        return self

    def set_html_body(self, html: str):
        self._email.html_body = html
        return self

    def add_attachment(self, filename: str):
        self._email.attachments.append(filename)
        return self

    def build(self):
        if not self._email.from_addr:
            raise ValueError("Отправитель не указан")
        if not self._email.to:
            raise ValueError("Нет получателя")
        if not self._email.subject:
            raise ValueError("Тема не указана")
        return self._email

class Director:
    def __init__(self, builder: EmailBuilder):
        self.builder = builder

    def build_welcome_email(self, to_addr: str, username: str):
        return (
            self.builder
                .set_from("noreply@company.com")
                .add_to(to_addr)
                .set_subject("Добро пожаловать, {}".format(username))
                .set_html_body(f"<h1>Здравствуйте, {username}!</h1>")
                .build()
        )

    def build_password_reset_email(self, to_addr: str, reset_link: str):
        return (
            self.builder
                .set_from("support@company.com")
                .add_to(to_addr)
                .set_subject("Сброс пароля")
                .set_html_body(f"<p>Перейдите по ссылке для сброса пароля: <a href='{reset_link}'>{reset_link}</a></p>")
                .build()
        )

if __name__ == "__main__":
    director = Director(EmailBuilder())
    email = director.build_welcome_email("user@example.com", "Иван")
    print(email)

    email2 = (
        EmailBuilder()
        .set_from("noreply@company.com")
        .add_to("client@example.com")
        .add_cc("manager@company.com")
        .set_subject("Ваш счёт №1234")
        .set_html_body("<h1>Счёт</h1>")
        .add_attachment("invoice_1234.pdf")
        .build()
    )
    print()
    print(email2)