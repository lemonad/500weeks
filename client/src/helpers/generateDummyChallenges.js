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
    "#eaeaea",
    "#eaeaea",
    "#eaeaea",
    "#eaeaea",
    "#eaeaea",
    "#eaeaea",
    "#eaeaea",
    "#eaeaea",
    "#eaeaea"
  ];
  const result = [];

  for (let i = 0; i < 10; i++) {
    result.push("#999999");
  }

  for (let i = 0; i < 150; i++) {
    const color = colors[Math.floor(Math.random() * colors.length)];
    result.push(color);
  }

  for (let i = 0; i < 340; i++) {
    result.push("#eaeaea");
  }

  return result;
};
