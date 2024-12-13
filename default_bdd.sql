CREATE TABLE servers (
    server_id INT PRIMARY KEY AUTO_INCREMENT,
    server_name VARCHAR(255),
    channel_id VARCHAR(255)
);

CREATE TABLE members (
    id_member INT PRIMARY KEY AUTO_INCREMENT,
    server_id INT,
    member_name VARCHAR(255),
    member_birthday_date VARCHAR(255),
    FOREIGN KEY (server_id) REFERENCES servers(server_id)
);

CREATE TABLE leaderboard (
    line_id INT PRIMARY KEY AUTO_INCREMENT,
    id_member INT,
    points INT,
    bonus INT,
    date_obtention DATE,
    FOREIGN KEY (id_member) REFERENCES members(id_member)
);

CREATE TABLE clips (
    id_clip INT PRIMARY KEY AUTO_INCREMENT,
    url VARCHAR(255)
);

CREATE TABLE last_clips (
    id_last_clip INT PRIMARY KEY AUTO_INCREMENT,
    id_clip INT,
    date_upload DATE,
    FOREIGN KEY (id_clip) REFERENCES clips(id_clip)
);

-- Insertion dans la table servers
INSERT INTO servers (server_name, channel_id) 
VALUES ('val', '1074125665512734770'),
       ('skynoz', '1231734938286559283'),
       ('flasteh', '960260059810648064');

-- Insertion dans la table members pour le serveur 'val'
INSERT INTO members (server_id, member_name, member_birthday_date) 
VALUES (1, 'Val', '03/05'),
       (1, 'Romane', '08/10'),
       (1, 'Birdy ', '19/12'),
       (1, 'Chloé ', '04/01'),
       (1, 'Richard ', '03/03'),
       (1, 'Yannick ', '07/07'),
       (1, 'Laura ', '30/09'),
       (1, 'Clo', '27/08'), 
       (1, 'Chris', '15/02'), 
       (1, 'Tommy', '09/07'), 
       (1, 'Marc', '25/02'), 
       (1, 'Baptiste', '14/03'), 
       (1, 'Lycos', '01/09'), 
       (1, 'Fanny', '10/05'), 
       (1, 'Vanille', '06/03'), 
       (1, 'Pierre', '25/04');

-- Insertion dans la table members pour le serveur 'skynoz'
INSERT INTO members (server_id, member_name, member_birthday_date) 
VALUES (2, 'Val', '03/05'),
       (2, 'Baptiste', '14/04'),
       (2, 'Scooby-doo de Lycos', '09/04'),
       (2, 'Brian', '01/09'),
       (2, 'Alix', '08/02'),
       (2, 'Trytox', '02/02'),
       (2, 'Weebzard', '27/04'),
       (2, 'Bastien', '12/02'),
       (2, 'Xarwin', '07/11'),
       (2, 'Mael', '16/09'),
       (2, 'Lightingloyz', '18/09'),
       (2, 'Kuzuha', '16/12');

-- Insertion dans la table members pour le serveur 'flasteh'
INSERT INTO members (server_id, member_name, member_birthday_date) 
VALUES (3, 'Casoar', '04/01'),
       (3, 'CharleLee', '01/05'),
       (3, 'Iof', '19/04'),
       (3, 'Sinon', '19/04'),
       (3, 'Banane', '11/06'),
       (3, 'Thesmans', '13/06'),
       (3, 'Ulta', '27/06'),
       (3, 'Prop', '03/07'),
       (3, 'Marie Christine', '13/07'),
       (3, 'Afalowna', '13/08'),
       (3, 'Raspi', '06/09'),
       (3, 'FlasTEH', '08/09'),
       (3, 'Telecar', '08/10'),
       (3, 'Evyf', '10/11'),
       (3, 'Saymel', '09/12'),
       (3, 'Kuzuha', '16/12'),
       (3, 'Warex', '24/12'),
       (3, 'Nethna', '28/04'),
       (3, 'Theynir', '20/12'),
       (3, 'Biotyc', '15/12'),
       (3, 'Val', '03/05');

-- Insertion dans la table clips
INSERT INTO clips (url) 
VALUES ('https://example.com/clip1.mp4'),
       ('https://example.com/clip2.mp4'),
       ('https://example.com/clip3.mp4');
