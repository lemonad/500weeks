DELETE FROM user;
DELETE FROM goal;
DELETE FROM challenge;
DELETE FROM week_challenge;

INSERT INTO user (id, username, first_name, last_name, email)
       VALUES (1, 'lemonad', 'Jonas', 'Nockert', 'jonasnockert@gmail.com');

INSERT INTO goal (id, title, subtitle, description, color, image_url)
       VALUES (1, 'Ingen fattigdom', 'Avskaffa all form av fattigdom överallt.', '', 'e5243b', '');
INSERT INTO goal (id, title, subtitle, description, color, image_url)
       VALUES (2, 'Ingen hunger', 'Avskaffa hunger, uppnå tryggad livsmedelsförsörjning, uppnå en bättre kosthållning och främja ett hållbart jordbruk.', '', 'dda63a', '');
INSERT INTO goal (id, title, subtitle, description, color, image_url)
       VALUES (3, 'Hälsa och välbefinnande', 'Säkerställa att alla kan leva ett hälsosamt liv och verka för alla människors välbefinnande i alla åldrar.', '', '4c9f38', '');
INSERT INTO goal (id, title, subtitle, description, color, image_url)
       VALUES (4, 'God utbildning för alla', 'Säkerställa en inkluderande och jämlik utbildning av god kvalitet och främja livslångt lärande för alla.', '', 'c5192d', '');
INSERT INTO goal (id, title, subtitle, description, color, image_url)
       VALUES (5, 'Jämställdhet', 'Uppnå jämställdhet, och alla kvinnors och flickors egenmakt.', '', 'ff3a21', '');

INSERT INTO challenge (id, goal_id, title, subtitle, description, image_url)
       VALUES (1, 1, 'Gå en kilometer om dagen', 'Förbättra din hälsa på lång sikt', '', '');

INSERT INTO week_challenge (id, week_no, user_id, challenge_id)
       VALUES (1, 1, 1, 1);
