# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Arizet")
define t = Character("Tarenza")
define y = Character("Ayata")
define g = Character("Graypaw")
define s = Character("Guard")


# The game starts here.
label start:

    scene flat

    "It's colder than usual for spring today."

    "Then again, it's still early."

    "My magic lessons with Ayata start an hour past dawn."

    "Ugh."

    "Whenever I don't want to get out of bed, I remind myself this is what I wanted."

    "To come to Suren. To study under Ayata, the Great Witch."

    "She's known not just as the Advisor of Magic to the King and Queen of Suren, but she's also respected as a powerful witch and scholar of magic throughout the neighboring nations."

    "That's why I cam all the way from Badour. Even though we have witches back home, we don't have the same tradition of scholastic witchcraft that Suren does."

    "But even Suren is not what it used to be--the only thing left of the once great University is a decrepit mage tower on the far side of the city."

    "I make sure I have all the books and materials I need before I leave."

    jump magic_lesson

    return
