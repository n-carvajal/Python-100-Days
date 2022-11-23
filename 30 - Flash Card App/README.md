# 100 Days of Python Code

## Project 31: French Vocabulary Flash Card App

### Brief

Create an app that displays vocabulary cards to the user.

* The front of the card should display a word in French.
* The back of the card should display the corresponding word in English.
* The front of the card should be displayed for a specific amount of seconds after which the back of the card will be shown.
* A new card should be displayed every time the user clicks on either the 'checkmark' or 'cancel' buttons.
* The user should be able to ask for a new card at any moment during the display cycle.
* Every time a new card is displayed the front should be shown for a specific amount of seconds after which the back of the card should be shown.
* If a new card is triggered by the user clicking the 'checkmark' button, the previous shown card should be removed from the list of cards to be shown in the future.
* If a new card is triggered by the user clicking the 'cancel' button, the previous card should remain in the group of cards to be shown in the future.
* If the app is closed, it should remember which words have previously been removed and not include them in the list of cards to be shown.

### Changing Language

The app uses `data/all_word_pairs.csv` as its starting word pairs data set. Presently the word pairs are in the form 'French to English'. The user can easily replace the contents of this file with any language combination of their choosing. The only caveats to this are:

* The data must be in 'csv' format.
* The first column of the data must be for the foreign language words and the second column for their native counterparts.
* The data must start with a header line stating the name of the foreign and native language.
* The following lines within `def foreign_word()` must be altered by changing the value **"French"** to the name of the header for the foreign language in the new `data/all_word_pairs.csv`:
  * `fgn_word = WORD_PAIR["French"]`
  * `card_cnv.itemconfig(card_language_lbl, text="French", fill="black")`
* The following lines within `def native_word()` must be altered by changing the value **"English"** to the name of the header for the native language in the new `data/all_word_pairs.csv`:
  * `ntv_word = WORD_PAIR["English"]`
  * `card_cnv.itemconfig(card_language_lbl, text="English", fill="black")`

### Setting Display Time

The amount of time for which to display the front of a card can be modified by changing the value for `display_time` at the `# Constants` section.  Note the value is represented in milliseconds.
