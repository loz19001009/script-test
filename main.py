local Player = game.Players.LocalPlayer
local Character = Player.Character or Player.CharacterAdded:Wait()
local HumanoidRootPart = Character:WaitForChild("HumanoidRootPart")

local flying = true -- Mặc định bật chế độ bay
local speed = 50 -- Tốc độ bay
local bodyGyro = Instance.new("BodyGyro", HumanoidRootPart)
local bodyVelocity = Instance.new("BodyVelocity", HumanoidRootPart)

-- Cài đặt BodyGyro và BodyVelocity
bodyGyro.P = 9e4
bodyGyro.MaxTorque = Vector3.new(9e4, 9e4, 9e4)
bodyGyro.CFrame = HumanoidRootPart.CFrame

bodyVelocity.MaxForce = Vector3.new(9e4, 9e4, 9e4)
bodyVelocity.Velocity = Vector3.zero

local UserInputService = game:GetService("UserInputService")
local RunService = game:GetService("RunService")

-- Bảng lưu trạng thái phím
local keys = {
    W = false,
    A = false,
    S = false,
    D = false
}

-- Xử lý sự kiện khi nhấn phím
UserInputService.InputBegan:Connect(function(input, gameProcessed)
    if gameProcessed then return end
    local key = input.KeyCode
    if key == Enum.KeyCode.W then keys.W = true end
    if key == Enum.KeyCode.A then keys.A = true end
    if key == Enum.KeyCode.S then keys.S = true end
    if key == Enum.KeyCode.D then keys.D = true end
end)

-- Xử lý sự kiện khi nhả phím
UserInputService.InputEnded:Connect(function(input)
    local key = input.KeyCode
    if key == Enum.KeyCode.W then keys.W = false end
    if key == Enum.KeyCode.A then keys.A = false end
    if key == Enum.KeyCode.S then keys.S = false end
    if key == Enum.KeyCode.D then keys.D = false end
end)

-- Hàm xử lý bay
RunService.RenderStepped:Connect(function()
    if flying then
        local moveDirection = Vector3.zero

        if keys.W then
            moveDirection = moveDirection + workspace.CurrentCamera.CFrame.LookVector
        end
        if keys.S then
            moveDirection = moveDirection - workspace.CurrentCamera.CFrame.LookVector
        end
        if keys.A then
            moveDirection = moveDirection - workspace.CurrentCamera.CFrame.RightVector
        end
        if keys.D then
            moveDirection = moveDirection + workspace.CurrentCamera.CFrame.RightVector
        end

        bodyVelocity.Velocity = moveDirection * speed
        bodyGyro.CFrame = workspace.CurrentCamera.CFrame
    else
        bodyVelocity.Velocity = Vector3.zero
    end
end)
