import HYRequest from "../request";

export const getPythonData = () => {
  return HYRequest.get({
    url: "/api/python",
  });
};
