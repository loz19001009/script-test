local Player = game.Players.LocalPlayer
local Character = Player.Character or Player.CharacterAdded:Wait()
local HumanoidRootPart = Character:WaitForChild("HumanoidRootPart")
local Humanoid = Character:WaitForChild("Humanoid")

local speed = 50 -- Tốc độ bay
local flying = true -- Mặc định là bay

-- Tạo BodyGyro và BodyVelocity
local bodyGyro = Instance.new("BodyGyro", HumanoidRootPart)
local bodyVelocity = Instance.new("BodyVelocity", HumanoidRootPart)

bodyGyro.P = 9e4
bodyGyro.MaxTorque = Vector3.new(9e4, 9e4, 9e4)
bodyGyro.CFrame = HumanoidRootPart.CFrame

bodyVelocity.MaxForce = Vector3.new(9e4, 9e4, 9e4)
bodyVelocity.Velocity = Vector3.zero

-- Hàm xử lý bay
game:GetService("RunService").RenderStepped:Connect(function()
    if flying then
        -- Lấy hướng di chuyển từ joystick (MoveDirection)
        local moveDirection = Humanoid.MoveDirection
        if moveDirection.Magnitude > 0 then
            bodyVelocity.Velocity = moveDirection * speed
        else
            bodyVelocity.Velocity = Vector3.zero
        end

        -- Đặt hướng nhìn theo camera
        bodyGyro.CFrame = workspace.CurrentCamera.CFrame
    end
end)
