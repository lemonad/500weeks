export const generateDummyChallenges = () => {
  const colors = [
    "#e5233d",
    "#dda73a",
    "#4ca146",
    "#27bfe6",
    "#fbc412",
    "#f26a2e",
    "#bf8d2c",
    "#407f46",
    "#136a9f",
    "#ffffff",
    "#ffffff",
    "#ffffff",
    "#ffffff",
    "#ffffff",
    "#ffffff",
    "#ffffff",
    "#ffffff",
    "#ffffff"
  ];
  const result = [];
  for (let i = 0; i < 500; i++) {
    const color = colors[Math.floor(Math.random() * colors.length)];
    result.push(color);
  }
  return result;
};
