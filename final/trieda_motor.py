"""Trieda na pracu s motormi."""
from machine import Pin
from machine import PWM
import time
# import sys


class Motor:
    """Tato trieda sluzi na pracu  motormi."""

    def __init__(self) -> None:
        """
        Konstruktor triedy.

        :param: None
        :return: None
        """
        self.AIN1 = PWM(Pin(10), freq = 1000, duty = 0)
        self.BIN1 = PWM(Pin(11), freq = 1000, duty = 0)
        self.AIN2 = PWM(Pin(13), freq = 1000, duty = 0)
        self.BIN2 = PWM(Pin(12), freq = 1000, duty = 0)

    def lavy_motor_dopredu(self, rychlost: int) -> None:
        """
        Tato funkcia aktivuje pohyb laveho motora dopredu.

        :param rychlost: int
        :return: None

        Parametre:
        - prvy parameter je rychlost s ktorou sa bude pohybovat lavy motor dopredu.
        Hodnota tohto parametra musi byt v rozsahu 0 az 1023
        """
        if rychlost > 1023:
            rychlost = 1023
        if rychlost < 0:
            rychlost = 0

        self.AIN2.duty(0)
        self.BIN2.duty(0)

        self.AIN2.duty(rychlost)
        self.BIN2.duty(0)

    def lavy_motor_dozadu(self, rychlost: int) -> None:
        """
        Tato funkcia aktivuje pohyb laveho motora dozadu.

        :param rychlost: int
        :return: None

        Parametre:
        - prvy parameter je rychlost s ktorou sa bude pohybovat lavy motor dozadu.
        Hodnota tohto parametra musi byt v rozsahu 0 az 1023
        """
        if rychlost > 1023:
            rychlost = 1023
        if rychlost < 0:
            rychlost = 0

        self.AIN2.duty(0)
        self.BIN2.duty(0)

        self.AIN2.duty(0)
        self.BIN2.duty(rychlost)

    def pravy_motor_dopredu(self, rychlost: int) -> None:
        """
        Tato funkcia aktivuje pohyb praveho motora dopredu.

        :param rychlost: int
        :return: None

        Parametre:
        - prvy parameter je rychlost s ktorou sa bude pohybovat pravy motor dopredu.
        Hodnota tohto parametra musi byt v rozsahu 0 az 1023
        """
        if rychlost > 1023:
            rychlost = 1023
        if rychlost < 0:
            rychlost = 0

        self.AIN1.duty(0)
        self.BIN1.duty(0)

        self.AIN1.duty(rychlost)
        self.BIN1.duty(0)

    def pravy_motor_dozadu(self, rychlost: int) -> None:
        """
        Tato funkcia aktivuje pohyb praveho motora dozadu.

        :param rychlost: int
        :return: None

        Parametre:
        - prvy parameter je rychlost s ktorou sa bude pohybovat pravy motor dozadu.
        Hodnota tohto parametra musi byt v rozsahu 0 az 1023
        """
        if rychlost > 1023:
            rychlost = 1023
        if rychlost < 0:
            rychlost = 0

        self.AIN1.duty(0)
        self.BIN1.duty(0)

        self.AIN1.duty(0)
        self.BIN1.duty(rychlost)


# mot = Motor()
# 
# mot.pravy_motor_dopredu(512)
# time.sleep(3)
# mot.pravy_motor_dopredu(0)
# time.sleep(1)
# mot.pravy_motor_dozadu(512)
# time.sleep(3)
# mot.pravy_motor_dozadu(0)
# time.sleep(1)
# 
# mot.lavy_motor_dopredu(512)
# time.sleep(3)
# mot.lavy_motor_dopredu(0)
# time.sleep(1)
# mot.lavy_motor_dozadu(512)
# time.sleep(3)
# mot.lavy_motor_dozadu(0)
# time.sleep(1)
# 
# sys.exit(0)

