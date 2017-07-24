import { HarvesterAppPage } from './app.po';

describe('harvester-app App', () => {
  let page: HarvesterAppPage;

  beforeEach(() => {
    page = new HarvesterAppPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
