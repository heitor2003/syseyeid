CREATE DATABASE sys_eye_id

USE sys_eye_id

CREATE TABLE clinicas IF NOT EXISTS(
    id_clinica INT PRIMARY KEY,
    nome_clinica VARCHAR(100) NOT NULL,
    endereco_clinica VARCHAR(200) NOT NULL
);


CREATE TABLE medicos IF NOT EXISTS(
    id_medico INT PRIMARY KEY AUTOINCREMENT,
    nome_medico VARCHAR(100) NOT NULL,
    email_medico VARCHAR(100) NOT NULL,
    senha_medico VARCHAR(100) NOT NULL,
    clinica_medico INT,
    FOREIGN KEY (clinica_medico) REFERENCES clinicas(id_clinica)
);

CREATE TABLE paciente IF NOT EXISTS(
    cpf_paciente VARCHAR(11) PRIMARY KEY,
    nome_paciente VARCHAR(100) NOT NULL,
    email_paciente VARCHAR(100) NOT NULL,
    senha_paciente VARCHAR(100) NOT NULL,
    endereco_paciente VARCHAR(200) NOT NULL,
    clinica_paciente INT,
    medico_paciente INT,
    FOREIGN KEY (clinica_paciente) REFERENCES clinicas(id_clinica),
    FOREIGN KEY (medico_paciente) REFERENCES medico(id_medico)
);

CREATE TABLE exames IF NOT EXISTS(
    id_exame INT PRIMARY KEY,
    data_exame DATE NOT NULL,
    paciente VARCHAR(11) NOT NULL,
    clinica INT NOT NULL,
    medico INT NOT NULL,
    FOREIGN KEY (paciente) REFERENCES paciente(cpf_paciente),
    FOREIGN KEY (clinica) REFERENCES clinicas(id_clinica),
    FOREIGN KEY (medico) REFERENCES medicos(id_medico)
);