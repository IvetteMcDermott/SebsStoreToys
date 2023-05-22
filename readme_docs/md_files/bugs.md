- Shopping Cart: 
    It was displaying and empty cart and still allowing to go to checkout page.
    Fix: If empty now it gives a message on that, and checout link is hidden.

- User Icon:
    User icon hides partially behind the logo.
    Fix: No sort yet.

- The subcategories menu dropdown in store are toggle:
    They drop but wont close until the category that was click for open gets click again.
    In small screens it could accumulate and turn annoying.
    Fix: None. As it is expected toggle behaviour.

- No callable object:
    That error came up couple of time refering to forms.
    Fix: Remove the () after form sort it. This was down to autocomplete.
         It was edit functionality.

- QBuy button in store cards:
    It would show at different level for each card.
    Fix: Gave height to title, so push the next div with the button to same position.

- Template does not exist for checkout form:
    Access to checkout would give that error at early stages of the project.
    Fix: TA gave me direction to include the 'Crispyform_boostrap4' in installed apps.

- Webhooks:
    They stopped working everywhile. This was down to gitpod changing the port 8000 url.
    Fix: Update the endpoint when its need.