class Resume:
    def __init__(
        self,
        name: str,
        email: str,
        phone: str = "",
        summary: str = "",
        experience: list = None,
        education: list = None,
        skills: list = None,
        languages: list = None,
        certifications: list = None,
    ):
        self.name = name
        self.email = email
        self.phone = phone
        self.summary = summary
        self.experience = experience or []
        self.education = education or []
        self.skills = skills or []
        self.languages = languages or []
        self.certifications = certifications or []

    def __str__(self):
        return (
            f"=== {self.name} ===\n"
            f"Email: {self.email}\n"
            f"Телефон: {self.phone}\n"
            f"Обзор: {self.summary}\n"
            f"Опыт: {len(self.experience)} позиций\n"
            f"Образование: {len(self.education)} степеней\n"
            f"Навыки: {', '.join(self.skills)}\n"
            f"Языки: {', '.join(self.languages)}\n"
            f"Сертификаты: {', '.join(self.certifications)}\n"
        )

class ResumeBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._resume_data = {
            "name": "",
            "email": "",
            "phone": "",
            "summary": "",
            "experience": [],
            "education": [],
            "skills": [],
            "languages": [],
            "certifications": [],
        }
        return self

    def set_name(self, name: str):
        self._resume_data["name"] = name
        return self

    def set_email(self, email: str):
        self._resume_data["email"] = email
        return self

    def set_phone(self, phone: str):
        self._resume_data["phone"] = phone
        return self

    def set_summary(self, summary: str):
        self._resume_data["summary"] = summary
        return self

    def add_experience(self, experience: dict):
        self._resume_data["experience"].append(experience)
        return self

    def add_education(self, education: dict):
        self._resume_data["education"].append(education)
        return self

    def add_skill(self, skill: str):
        self._resume_data["skills"].append(skill)
        return self

    def add_language(self, language: str):
        self._resume_data["languages"].append(language)
        return self

    def add_certification(self, certification: str):
        self._resume_data["certifications"].append(certification)
        return self

    def build(self):
        resume = Resume(**self._resume_data)
        self.reset()
        return resume

class Director:
    def __init__(self, builder: ResumeBuilder):
        self._builder = builder

    def build_standard_resume(self, name: str, email: str):
        return (
            self._builder
                .set_name(name)
                .set_email(email)
                .set_summary("Опытный специалист в своей области.")
                .add_skill("Python")
                .add_skill("SQL")
                .add_experience({"company": "Yandex", "years": 3})
                .add_education({"degree": "Бакалавр", "school": "МГУ"})
                .build()
        )

    def build_extended_resume(self, name: str, email: str):
        return (
            self._builder
                .set_name(name)
                .set_email(email)
                .set_phone("+7-900-000-0000")
                .set_summary("Высококвалифицированный инженер.")
                .add_skill("Python")
                .add_skill("Docker")
                .add_skill("Machine Learning")
                .add_experience({"company": "Google", "years": 5})
                .add_experience({"company": "Facebook", "years": 2})
                .add_education({"degree": "Магистр", "school": "СПбГУ"})
                .add_language("Русский")
                .add_language("Английский")
                .add_certification("PMP")
                .build()
        )

builder = ResumeBuilder()
director = Director(builder)

resume1 = director.build_standard_resume("Анна Иванова", "anna@example.com")
print(resume1)

print("\n---\n")

resume2 = director.build_extended_resume("Петр Петров", "petr@example.com")
print(resume2)