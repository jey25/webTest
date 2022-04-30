describe("My First Test", () => {
    it("Visits the Kitchen Sink", () => {
      //cy.visit("url") 사용!
      cy.visit("https://example.cypress.io");
    });
  });