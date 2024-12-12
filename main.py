local Players = game:GetService("Players")
local RunService = game:GetService("RunService")

-- Tạo một hàm để cập nhật ESP cho tất cả người chơi
local function createESP(player)
    local character = player.Character
    if not character then return end
    
    -- Thêm một phần để làm sáng người chơi, ví dụ: một khung hình xung quanh họ
    local highlight = Instance.new("Highlight")
    highlight.Parent = character
    highlight.FillColor = Color3.fromRGB(255, 0, 0) -- Màu sắc viền
    highlight.OutlineColor = Color3.fromRGB(255, 255, 255) -- Màu sắc viền ngoài
    highlight.Thickness = 0.3 -- Độ dày của viền

    -- Khi nhân vật thay đổi, ta cũng sẽ cập nhật ESP
    character:WaitForChild("HumanoidRootPart")
end

-- Đảm bảo rằng mỗi người chơi đều có ESP
Players.PlayerAdded:Connect(function(player)
    player.CharacterAdded:Connect(function()
        createESP(player)
    end)
end)

-- Thêm ESP cho những người chơi đã có mặt khi script bắt đầu
for _, player in ipairs(Players:GetPlayers()) do
    if player.Character then
        createESP(player)
    end
end

-- Đảm bảo cập nhật liên tục
RunService.RenderStepped:Connect(function()
    for _, player in ipairs(Players:GetPlayers()) do
        if player.Character then
            local highlight = player.Character:FindFirstChildOfClass("Highlight")
            if highlight then
                -- Cập nhật lại vị trí nếu cần thiết (chắc chắn người chơi được theo dõi)
                highlight.Adornee = player.Character
            end
        end
    end
end)
