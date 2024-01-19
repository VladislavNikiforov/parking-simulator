import pygame
import sys
import math
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
import os
import random


chromeService = Service()
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("-headless")
driver = webdriver.Chrome(service=chromeService, options=chromeOptions)

def scrapParameters(autoFullName):
    # managing web-browser settings

    # acessing hashing calculator through web-browser
    url = "https://www.automobiledimension.com"
    driver.get(url)
    time.sleep(3)
    name = autoFullName.split()[0]
    brandSelector = "a[title='" + name + "']" #selector value "a[title='Audi']"
    autoBrandElement= driver.find_element(By.CSS_SELECTOR, brandSelector)
    #
    autoBrandurl = autoBrandElement.get_attribute("href")
    driver.get(autoBrandurl)

    dimemnsionXSelector = "//div[h2[text()='" + autoFullName + "']]//span[contains(@class, 'marquespais')]"
    wait = WebDriverWait(driver, 10)
    dimensions_span = wait.until(EC.presence_of_element_located((By.XPATH, dimemnsionXSelector)))
    dimensions_text = driver.execute_script("return arguments[0].textContent;", dimensions_span)
    length, width, _ = map(int, re.findall(r'\d+', dimensions_text))

    #print(f"Length: {length} mm, Width: {width} mm")
    return length//100, width//100 #in dm (similar to pxl)

class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((820, 440))
        pygame.display.set_caption("Autostāvvietas simulators")
        self.font = pygame.font.Font(None, 36)
        self.background_image = pygame.image.load('background.png')

        self.input_rects = [pygame.Rect(100, 150, 320, 30), pygame.Rect(100, 230, 320, 30)]
        self.input_texts = ["", ""]
        self.playerCarModel = ""
        self.numAutos = 0

        self.start_button = pygame.Rect(100, 300, 200, 50)
        self.exit_button = pygame.Rect(100, 370, 200, 50)

    def run(self):
        running = True
        active_input = None
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.start_button.collidepoint(mouse_pos):
                        self.playerCarModel = self.input_texts[0]
                        self.numAutos = int(self.input_texts[1])
                        return True
                    if self.exit_button.collidepoint(mouse_pos):
                        return False
                    for i, rect in enumerate(self.input_rects):
                        if rect.collidepoint(mouse_pos):
                            active_input = i
                            break
                elif event.type == pygame.KEYDOWN and active_input is not None:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_texts[active_input] = self.input_texts[active_input][:-1]
                    else:
                        self.input_texts[active_input] += event.unicode  
            self.draw_menu()

    def draw_text(self, text, position, color=(255, 255, 255)):
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, position)

    def draw_menu(self):
        self.screen.blit(self.background_image, (0, 0))

        start_button = pygame.Rect(100, 300, 200, 50)
        exit_button = pygame.Rect(100, 370, 200, 50)
        pygame.draw.rect(self.screen, (0, 128, 0), start_button)  
        pygame.draw.rect(self.screen, (128, 0, 0), exit_button)  

        self.draw_text("Starts", (start_button.x + 70, start_button.y + 15))
        self.draw_text("Izēja", (exit_button.x + 70, exit_button.y + 15))

        self.draw_text("Tavas mašīnas modelis:", (100, 120), (255, 255, 255))
        self.draw_text("Citu mašīnu skaits (0-20):", (100, 200), (255, 255, 255))

        for rect, text in zip(self.input_rects, self.input_texts):
            pygame.draw.rect(self.screen, (255, 255, 255), rect, 2)
            self.draw_text(text, (rect.x + 5, rect.y + 5), (255, 255, 255))

        pygame.display.flip()

class Cars:
    carList = [file for file in os.listdir('./cars') if (file.endswith('.png') or file.endswith('.jpg'))]
    print(carList)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        car_image = random.choice(self.carList)
        self.width, self.height = scrapParameters(car_image.split('.')[0])
        self.width *=2
        self.height *=2
        filepath = "cars/" + car_image
        self.image = pygame.image.load(filepath)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    #update rect for collission 
    def update(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.rect.w -= 4
        
class Player:
    def __init__(self, x, y, carModel, angle=0, speed=0, width=80, height=35):
        self.x = x
        self.y = y
        if carModel == "":
            self.width,  self.height = width, height
        else:
            self.width,  self.height = scrapParameters(carModel) #get length and width
            self.width *= 2
            self.height *= 2
        self.angle = angle
        self.speed = speed
        self.steering_angle = 0  
        self.max_steering_angle = 45 
        self.turning_speed = 3 
        self.alignment_speed = 0.5 
        self.max_speed = 5
        self.min_speed = -5  
        self.is_reversing = False  
        self.brake_speed = 0.15
        self.stopping_threshold = 0.1  
       
        CarPath = "cars/" + carModel + ".png"
        try:
            self.image = pygame.image.load(CarPath)  
        except:
            self.image = pygame.image.load('cars/Audi A4.png')

        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.width = self.rect.width
        self.height = self.rect.height

    def checkBorder(self):
        if self.x < 15:
            self.x = 15
            self.speed = 0
        elif self.x > ParkingScreen.WIDTH - 10:
            self.x = ParkingScreen.WIDTH - 10
            self.speed = 0

        if self.y < 15:
            self.y = 15
            self.speed = 0
        elif self.y > ParkingScreen.HEIGHT - self.height/2:
            self.y = ParkingScreen.HEIGHT - self.height/2
            self.speed = 0
    
    def updateAlignment(self):
        # Car wheel alignment
        if -self.alignment_speed < self.steering_angle < self.alignment_speed:
            self.steering_angle = 0
        #elif self.steering_angle > 0:
        #    self.steering_angle -= self.alignment_speed
        #elif self.steering_angle < 0:
        #    self.steering_angle += self.alignment_speed
    
    def updateAngleAndVelocity(self):
       #update speed and angle
        if self.steering_angle != 0:
            turning_radius = 50 / math.sin(math.radians(self.steering_angle))
            angular_velocity = self.speed / turning_radius
        else:
            angular_velocity = 0

        self.angle += math.degrees(angular_velocity)
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle)) 

    def update(self):
        self.checkBorder()
        self.updateAlignment()
        self.updateAngleAndVelocity()
        #update rect for collission
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.rect.w -= 30
        self.rect.h -= 15

    def accelerate(self):
        if self.is_reversing:
            if self.speed > self.min_speed:
                self.speed -= 0.05
        else:
            if self.speed < self.max_speed:
                self.speed += 0.05

    def brake(self):
         # moderate brake
        if self.speed > 0:
            if self.speed < self.stopping_threshold:
                self.speed = 0
            else:
                self.speed -= self.brake_speed
        elif self.speed < 0:
            if self.speed > -self.stopping_threshold:
                self.speed = 0
            else:
                self.speed += self.brake_speed

    def turn_left(self):
        if self.steering_angle > -self.max_steering_angle:
            self.steering_angle -= self.turning_speed

    def turn_right(self):
        if self.steering_angle < self.max_steering_angle:
            self.steering_angle += self.turning_speed

    def draw(self, screen):
        # Rotate the car image and then draw it
        rotated_image = pygame.transform.rotate(self.image, -self.angle)
        new_rect = rotated_image.get_rect(center=self.rect.center)
        new_rect.center = (self.x, self.y)
        screen.blit(rotated_image, new_rect.topleft)

    def reverse(self):
        if self.speed == 0:
            self.is_reversing = not self.is_reversing

    def display_info(self, screen):
        font = pygame.font.SysFont("Arial", 20)
        speed_text = font.render(f"Ātrums: {self.speed*10:.2f} km/h", True, (0, 0, 0))
        reverse_text = font.render(f"Reverse: {'Jā' if self.is_reversing else 'Nē'}", True, (0, 0, 0))
        st_angl_text = font.render(f"Stūres lenķis: {self.steering_angle:.2f}", True, (0, 0, 0))

        screen.blit(speed_text, (10, 10))
        screen.blit(reverse_text, (10, 35))
        screen.blit(st_angl_text, (10, 60))

    def parking(self, parkingSpace):
        return parkingSpace.check_parking(self.image.get_rect(center=(self.x, self.y)))

class ParkingScreen:
     # define colours and parms
    WHITE = (255, 255, 255)
    GREY = (200, 200, 200)
    WIDTH, HEIGHT = 1100, 440
    PARKING_SPACE_WIDTH = 110
    PARKING_SPACE_HEIGHT = 46   
    SPACING = 20

    def __init__(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Autostāvvietas simulators")
        self.static_surface = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.static_surface.fill(self.WHITE)
        self.draw_parking_lot()

    def draw_parking_lot(self):
        for row in range(1, 5):
            for col in range(8):
                if col in [0, 2, 5, 7]:
                    continue
                pygame.draw.rect(self.static_surface, self.GREY, 
                                 [(self.PARKING_SPACE_WIDTH + self.SPACING) * col + self.SPACING,
                                  (self.PARKING_SPACE_HEIGHT + self.SPACING) * row + self.SPACING,
                                  self.PARKING_SPACE_WIDTH, self.PARKING_SPACE_HEIGHT])

    def create_cars(self, num_cars):
        cars = []
        parking_spots = []

        # parking spot list
        for row in range(1, 5):
            for col in range(8):
                if col in [0, 2, 5, 7]:
                    continue  # skip central columns
                x = (self.PARKING_SPACE_WIDTH + self.SPACING) * col + self.SPACING + self.PARKING_SPACE_WIDTH // 2
                y = (self.PARKING_SPACE_HEIGHT + self.SPACING) * row + self.SPACING + self.PARKING_SPACE_HEIGHT // 2
                parking_spots.append((x, y))

        # random car spawn in parking spots
        for _ in range(min(num_cars, len(parking_spots))):
            x, y = random.choice(parking_spots)
            parking_spots.remove((x, y))  # delete spot which is already occupied
            car = Cars(x, y)
            cars.append(car)
        # draw static surface
        for car in cars:
            car.draw(self.static_surface)

        return cars
    
    def check_parking(self, car_rect):
        for row in range(1, 5):
            for col in range(8):
                if col in [0, 2, 5, 7]:
                    continue  # skip central column
                parking_spot_rect = pygame.Rect(
                    (self.PARKING_SPACE_WIDTH + self.SPACING) * col + self.SPACING,
                    (self.PARKING_SPACE_HEIGHT + self.SPACING) * row + self.SPACING,
                    self.PARKING_SPACE_WIDTH+20, self.PARKING_SPACE_HEIGHT+15
                )
                if parking_spot_rect.contains(car_rect):
                    return True
        return False
        
    def play_explosion_animation(screen, explosion_images, position, clock):
        for image in explosion_images:
            screen.blit(image, position)
            pygame.display.flip()
            clock.tick(15)  # animation speed

def main():
    pygame.mixer.init()

    # upload sound file
    collision_sound = pygame.mixer.Sound('bang.wav')
    explosion_images = pygame.image.load('bang.png')

    pygame.init()
    #cretate menu object 
    gameMenu = Menu()
    if gameMenu.run():

        #create player object
        car = Player(50, 50, gameMenu.playerCarModel)
        parkingSpace = ParkingScreen()
        autos = parkingSpace.create_cars(gameMenu.numAutos)
        driver.quit() #driver quit
    
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        car.reverse()
                    elif event.key == pygame.K_p:
                        if car.parking(parkingSpace):
                            end_button = pygame.Rect(410, 220, 280, 50)
                            pygame.draw.rect(parkingSpace.screen, (0, 128, 0), end_button)
                            gameMenu.draw_text("Eksamens nokartots!", (end_button.x + 10, end_button.y + 15), (0, 0, 0))
                            pygame.display.flip()
                            time.sleep(5)
                            running = False
            
            parkingSpace.screen.blit(parkingSpace.static_surface, (0, 0))
                
            pygame.display.flip()
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                car.accelerate()
            if keys[pygame.K_b]:
                car.brake()
            if keys[pygame.K_q]:
                car.turn_left()
            if keys[pygame.K_e]:
                car.turn_right()

            car.update()
            #collison check
            for auto in autos:
                auto.update()
                if car.rect.colliderect(auto.rect):
                    collision_sound.play()
                    parkingSpace.screen.blit(explosion_images, (auto.x, auto.y))
                    pygame.display.flip()
                    clock.tick(15)
                    car.speed = 0

            car.draw(parkingSpace.screen)

            car.display_info(parkingSpace.screen)

            pygame.display.flip()
            clock.tick(30)
    else:
        pygame.quit()
        sys.exit()
if __name__ == "__main__":
    main()
