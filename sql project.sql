create database Cinebase;
use Cinebase;

create table users(
user_id INT AUTO_INCREMENT PRIMARY KEY,
username varchar(100) UNIQUE NOT NULL,
password varchar(8) NOT NULL,
email varchar(50) UNIQUE NOT NULL);
insert into users values(6,"seeth","123seeth","seeth@example.com");
select * from users;

create table movies(
movie_id int AUTO_INCREMENT PRIMARY KEY,
title varchar(50) not null,
genre varchar(50),
release_year int);
alter table movies drop column release_year;
alter table movies add column release_year int;

INSERT INTO movies (title, genre, release_year) VALUES
('Pushpa 2: The Rule', 'Action', 2024),
('Kalki 2898 AD', 'Sci-Fi', 2024),
('Devara: Part 1', 'Action', 2024),
('Hanu-Man', 'Superhero', 2024),
('Guntur Kaaram', 'Drama', 2024),
('Tillu Square', 'Comedy', 2024),
('Lucky Baskhar', 'Thriller', 2024),
('Saripodhaa Sanivaaram', 'Action', 2024),
('KA', 'Mystery', 2024),
('Naa Saami Ranga', 'Drama', 2024),
('Game Changer', 'Action', 2025),
('Daaku Maharaaj', 'Action', 2025),
('HIT: The Third Case', 'Thriller', 2025),
('Thandel', 'Drama', 2025),
('Mad Square', 'Comedy', 2025),
('Court', 'Drama', 2025),
('Single', 'Romance', 2025),
('Arjun Son of Vyjayanthi', 'Action', 2025),
('Jack', 'Drama', 2025),
('Sankranthiki Vasthunam', 'Action', 2025);

select * from movies;

create table reviews(
review_id int AUTO_INCREMENT PRIMARY KEY,
user_id int, 
movie_id int,
rating int,
comments varchar(500),
FOREIGN KEY (user_id) REFERENCES users(user_id),
FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);


ALTER TABLE reviews
MODIFY rating INT CHECK (rating BETWEEN 1 AND 5);


INSERT INTO users (username, password, email) VALUES
('Mahi', 'Mahi123', 'mahi@example.com'),
('Ram', 'Ram123', 'ram@example.com'),
('Vidya', 'Vid45', 'vidya@example.com'),
('Yuvaraj', 'yuva123', 'yuvaraj@example.com'),
('Yugandhar', 'yug123', 'yugandhar@example.com');

select * from users;


INSERT INTO reviews (user_id, movie_id, rating, comments) VALUES
(1, 1, 5, 'Pushpa 2 is a powerful sequel with great action.'),
(2, 2, 4, 'Kalki 2898 AD had an epic feel, really cool visuals.'),
(3, 3, 3, 'Devara had promise but pacing was uneven.'),
(4, 4, 5, 'Hanu-Man was a refreshing superhero experience.'),
(5, 5, 4, 'Guntur Kaaram had solid performances.'),
(1, 6, 4, 'Tillu Square was lighthearted and fun.'),
(2, 7, 5, 'Lucky Baskhar was thrilling and unique.'),
(3, 8, 3, 'Saripodhaa Sanivaaram was decent but could be better.'),
(4, 9, 4, 'KA kept me guessing till the end.'),
(5, 10, 3, 'Naa Saami Ranga was slow but emotional.'),
(1, 11, 5, 'Game Changer looks promising!'),
(2, 12, 4, 'Daaku Maharaaj was gripping.'),
(3, 13, 4, 'HIT: The Third Case had strong mystery elements.'),
(4, 14, 3, 'Thandel felt predictable at times.'),
(5, 15, 4, 'Mad Square was quirky and fun.');

select * from reviews;

select * from movies where release_year = 2010;

SELECT 
    movies.title, 
    movies.genre,
    reviews.rating,
    movies.release_year 
FROM 
    reviews 
INNER JOIN 
    movies 
ON 
    reviews.movie_id = movies.movie_id 
ORDER BY 
    reviews.rating DESC;
    
select * from reviews;
select * from movies;
select * from users;
delete from users where username = "Ganesh";