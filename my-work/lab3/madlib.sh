#!/bin/bash


clear
echo "Let's build a mad-lib!"

read -p "1. Name a cartoon character (noun): " NOUN1
read -p "2. Name a dessert (noun): " NOUN2
read -p "3. Name a mode of transport (verb): " VERB1
read -p "4. Name a creative activity (verb): " VERB2
read -p "5. Describe a celebrity crush (adjective): " ADJ1
read -p "6. Describe a fictional character (adjective): " ADJ2
read -p "7. Describe how your day ended today (adverb): " ADVERB1
read -p "8. Describe how often you exercise (adverb): " ADVERB2

echo "Once upon a time, $NOUN1 loved to eat $NOUN2"
echo "$NOUN1 would always $VERB1 to eat $NOUN2, and they loved to $VERB2 $NOUN2"
echo "One day, $NOUN1 met an especially $ADJ1 and $ADJ2 $NOUN2"
echo "That day, $NOUN1's day ended $ADVERB1, so they were excited to see $NOUN2"
echo "$NOUN1's $ADVERB2 excerise paid off, and they ran to eat $NOUN2"
