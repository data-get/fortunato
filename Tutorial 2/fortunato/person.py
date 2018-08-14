import random


class Person():
    """
    A Person object used to construct a fortune
    """
    FORTUNES = [
        'A beautiful, smart, and loving person will be coming into your life.',
        'A dubious friend may be an enemy in camouflage.',
        'A faithful friend is a strong defense.',
        'A feather in the hand is better than a bird in the air.',
        'A fresh start will put you on your way.',
        'A friend asks only for your time not your money.',
        'A friend is a present you give yourself.',
        'A gambler not only will lose what he has, but also will lose what he doesn’t have.',  # noqa: E501
        'A golden egg of opportunity falls into your lap this month.',
        'A good friendship is often more important than a passionate romance.',
        'A good time to finish up old tasks.',
        'A hunch is creativity trying to tell you something.',
        'A lifetime friend shall soon be made.',
        'A lifetime of happiness lies ahead of you.',
        'A light heart carries you through all the hard times.',
        'A new perspective will come with the new year.',
        'A person is never to (sic) old to learn.',
        'A person of words and not deeds is like a garden full of weeds.',
        'A pleasant surprise is waiting for you.',
        'A short pencil is usually better than a long memory any day.',
        'A small donation is call for. It’s the right thing to do.',
        'A smile is your personal welcome mat.',
        'A smooth long journey! Great expectations.',
        'A soft voice may be awfully persuasive.',
        'A truly rich life contains love and art in abundance.',
        'Accept something that you cannot change, and you will feel better.',
        'Adventure can be real happiness.',
        'Advice is like kissing. It costs nothing and is a pleasant thing to do.',  # noqa: E501
        'Advice, when most needed, is least heeded.',
        'All the effort you are making will ultimately pay off.',
        'All the troubles you have will pass away very quickly.',
        'All will go well with your new project.',
        'All your hard work will soon pay off.',
        'Allow compassion to guide your decisions.',
        'An acquaintance of the past will affect you in the near future.',
        'An agreeable romance might begin to take on the appearance.',
        'An important person will offer you support.',
        'An inch of time is an inch of gold.',
        'Any decision you have to make tomorrow is a good decision.',
        'At the touch of love, everyone becomes a poet.',
        'Be careful or you could fall for some tricks today.',
        'Beauty in its various forms appeals to you.',
        'Because you demand more from yourself, others respect you deeply.',
    ]

    def __init__(self, name, age, random_lib=None):
        self.name = name
        self.age = age

        if random_lib is None:
            random_lib = random
        self.random_lib = random_lib

    def get_fortune(self):
        return self.random_lib.choice(self.FORTUNES)
