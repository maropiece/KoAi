CREATE DATABASE IF NOT EXISTS MochiScan;
USE MochiScan;
CREATE TABLE examples (
  id INT AUTO_INCREMENT PRIMARY KEY,
  product_name VARCHAR(100),
  description TEXT,
  safety_score INT,
  verdict ENUM('Safe', 'Moderate', 'Caution')
);
select * from examples;
USE MochiScan;

INSERT INTO examples (product_name, description, safety_score, verdict) VALUES
('Skull Panda', 'AI-powered talking doll that interacts with children.', 42, 'Caution'),
('Hirono', 'Screen-free audio player for kids with story figures.', 87, 'Safe'),
('Talking Angela', 'Educational companion robot that supports emotional learning.', 76, 'Moderate'),
('Cozmo', 'Cute robot that plays games and expresses emotions.', 84, 'Safe'),
('Peach Riot', 'Emotion regulation plush that responds to touch.', 91, 'Safe'),
('CryBaby', 'Interactive robot designed for children with special needs.', 89, 'Safe'),
('Space Molly', 'Smart toy that talks and reacts to children’s behavior.', 62, 'Moderate'),
('Dimoo', 'Plush AI assistant for children with stories and questions.', 59, 'Moderate'),
('Molly', 'Interactive doll that answers questions using internet.', 34, 'Caution'),
('Labubu', 'Programmable ball robot for learning and fun.', 88, 'Safe'),
('Lafufu', 'Smart speaker with child-friendly content and parental controls.', 73, 'Moderate'),
('Zimomo', 'Virtual influencer interacting with kids online.', 28, 'Caution'),
('Tycoco', 'Home companion robot with smart capabilities.', 80, 'Safe'),
('Spooky', 'Learning robot designed for STEM basics.', 83, 'Safe'),
('Plucky', 'Smart plush that reads bedtime stories.', 90, 'Safe'),
('Kubo', 'Dancing robot with light and sound features.', 77, 'Moderate'),
('Pino Jelly', 'Screenless coding toy for preschoolers.', 95, 'Safe'),
('ZSIGA', 'Intro to robotics and coding for kids.', 92, 'Safe'),
('Sweet Bean', 'Mystery pet toy with behavioral AI.', 65, 'Moderate'),
('Yano', 'Animated storytelling robot.', 55, 'Moderate'),
('Pleo', 'Realistic baby dinosaur robot with emotional behaviors.', 82, 'Safe'),
('Paro', 'Furry AI seal for emotional comfort.', 94, 'Safe'),
('smiski', 'AI companion robot for education and safety.', 72, 'Moderate'),
('Sonny Angel', 'Cute home robot with child-friendly design.', 78, 'Moderate'),
('Hacipupu', 'Voice-controlled home assistant for kids.', 39, 'Caution');

select * from examples;

