// Greenhouse adapter - fills Greenhouse job application forms
module.exports = {
  name: 'greenhouse',
  matches: (url) => url.includes('greenhouse.io') || url.includes('boards.greenhouse.io'),
  async fill(page, payload) {
    const steps = [];
    const name = payload.contact?.full_name || '';
    const [first, ...rest] = name.split(' ');
    const last = rest.join(' ');
    const tryFill = async (selectors, value, label) => {
      for (const sel of selectors) {
        try {
          const el = await page.$(`input[name='${sel}'], input[id='${sel}']`);
          if (el && value) { await el.fill(value); steps.push({ field: label, status: 'ok' }); return; }
        } catch {}
      }
    };
    await tryFill(['first_name','fname'], first, 'first_name');
    await tryFill(['last_name','lname'], last, 'last_name');
    await tryFill(['email','email_address'], payload.contact?.email, 'email');
    await tryFill(['phone','phone_number'], payload.contact?.phone, 'phone');
    await tryFill(['linkedin_profile','linkedin'], payload.contact?.linkedin_url, 'linkedin');
    const coverEl = await page.$('textarea[name="cover_letter_text"]');
    if (coverEl && payload.content?.cover_letter) {
      await coverEl.fill(payload.content.cover_letter.substring(0, 2000));
      steps.push({ field: 'cover_letter', status: 'ok' });
    }
    return steps;
  }
};
