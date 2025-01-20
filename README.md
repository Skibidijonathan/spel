# Casino Spel - README

## Introduktion
Det här är ett Python-baserat casinospel där spelaren kan testa lyckan i tre olika spel:
1. **Slots**  
2. **Blackjack**  
3. **Roulette**  

### Spelregler
- Du börjar med **100 000 kronor** i startkapital.
- Du kan satsa pengar i varje spel:
  - Om du vinner, läggs din vinst till dina pengar.
  - Om du förlorar, dras din insats från dina pengar.
- Om du får slut på pengar måste du lämna casinot.

### Spelalternativ
#### Slots
- Snurra tre hjul med olika symboler.
- Om symbolerna matchar vinner du:
  - **Tre lika:** Största vinsten!
  - **Två lika:** Mindre vinst.
- Insatsen multipliceras beroende på resultatet.

#### Blackjack
- Målet är att få en hand som är så nära **21** som möjligt utan att gå över.
- Du spelar mot dealern:
  - Om du får **21** direkt vinner du blackjack.
  - Om din hand är närmare 21 än dealerns vinner du.
  - Om din hand överstiger 21 förlorar du.

#### Roulette
- Du kan satsa på:
  - Ett specifikt nummer (0–36).
  - Färg: **rött** eller **svart**.
  - Jämnt (**even**) eller udda (**odd**).
- Om resultatet matchar din satsning vinner du enligt olika odds.

## Installation
1. Ladda ner filen `casino.py`.
2. Se till att du har Python installerat (version 3.7 eller senare).
3. Kör spelet med kommandot:
   ```bash
   python casino.py
   ```

## Så här spelar du
1. Starta spelet och välj ett spel från huvudmenyn.
2. Följ instruktionerna på skärmen för att satsa och spela.
3. Spelet håller reda på ditt saldo och meddelar om du vinner eller förlorar.
4. När du vill avsluta spelet väljer du att gå hem.

## Begränsningar
- Spelet är textbaserat och saknar grafik.
- Inga funktioner för att spara framsteg.

## Förbättringsidéer
- Lägg till ett gränssnitt för att göra spelet visuellt mer engagerande.
- Implementera fler casinospel.
- Lägg till stöd för att spara och ladda spelarens framsteg.

Tack för att du spelar! Lycka till!
