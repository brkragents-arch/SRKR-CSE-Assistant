FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
COPY srkr_cse_workspace ./srkr_cse_workspace
EXPOSE 5000
ENV NODE_ENV=production
ENV PORT=5000
CMD ["node", "srkr_cse_workspace/portal/server.js"]
